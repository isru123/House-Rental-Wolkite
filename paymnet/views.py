
from datetime import datetime
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Payment
from django.utils import timezone
from .models import Notification
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Booking
from main.models import Listing
from .forms import TenantInfoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



@login_required
def CheckOut(request, product_id):
    product = Listing.objects.get(id=product_id)
    host = request.get_host()

    # Calculate system fee (0.2% of the product price)
    system_fee = round((0.2 / 100) * product.price, 2)

    # Calculate total price including system fee
    total_price = round(product.price + system_fee, 2)

    # Generate a UUID for the payment ID
    payment_id = uuid.uuid4().hex

    # Save payment information to the database
    # You need to adjust this based on your Payment model structure
    payment = Payment.objects.create(
        amount=total_price,
        payer=request.user,
        recipient=product.seller.user,
        payment_id=payment_id,
    )

    # Create a booking object
    # Adjust this based on your Booking model structure
    booking_date = timezone.now()  # Set booking date to current datetime
    booking = Booking.objects.create(
        tenant=request.user,
        house_id=product.id,
        house=product,
        total_price=total_price,
        booking_status='pending',
        payment_status='pending',
        confirmation_code=uuid.uuid4().hex,
        payment_id=payment_id,
        booking_date=booking_date,  # Set booking date here
      
    )

    # Send email notification to seller
    # Adjust this based on your email notification logic
    subject = 'Payment Received'
    # You need to adjust the email template path and context data
    html_message = render_to_string('payment/email_payment_notification.html', {'product': product})
    plain_message = strip_tags(html_message)
    from_email = 'fikefiresew1234@gmail.com'  # Update with your email address
    to_email = product.seller.user.email
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

    # PayPal checkout parameters
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': "{:.2f}".format(total_price),  # Format total_price to two decimal places
        'invoice': payment_id,
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
    }

    # Create PayPalPaymentsForm
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': product,
        'paypal': paypal_payment,
        'system_fee': "{:.2f}".format(system_fee),  # Format system_fee to two decimal places
        'total_price': "{:.2f}".format(total_price)  # Format total_price to two decimal places
    }

    return render(request, 'payment/checkout.html', context)



# @user_passes_test(lambda u: u.is_superuser)
def approve_payment(request, booking_id):
    # Get the booking object
    booking = get_object_or_404(Booking, id=booking_id)
    
    if booking.payment_status == 'pending':
        # Mark payment as paid
        booking.payment_status = 'paid'
        booking.save()
    
    # Redirect back to the admin page regardless of payment status
    return redirect('admin:paymnet_booking_changelist')



def confirm_booking(request, booking_id):
    # Get the booking object
    # Calculate refund based on days and seconds before booking date
    current_datetime = timezone.now()  # Current datetime

    booking = Booking.objects.get(id=booking_id)
    print("Booking date:", booking.booking_date)
    print("Current datetime:", current_datetime)
    # Confirm the booking (update booking_status)
    booking.booking_status = 'confirmed'
    booking.payment_status = 'paid'

    booking.save()
    return redirect('all_bookings') 




def change_booking_status(request, booking_id, new_status):
    # Get the booking object
    booking = Booking.objects.get(id=booking_id)
    # Update booking_status
    booking.booking_status = new_status
    booking.save()
    return redirect('all_bookings') 

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    subject = 'Booking Cancellation Notification'
    html_message = render_to_string('payment/email_cancel_notification.html', {
        'booking': booking,
        # Pass additional information here, such as house address or any other relevant details
        'house_address': booking.house.address if booking.house else 'N/A',
    })
    plain_message = strip_tags(html_message)
    from_email = 'fikefiresew1234@gmail.com'  # Update with your email address

    # Get superuser email
    superuser_email = User.objects.filter(is_superuser=True).first().email

    send_mail(subject, plain_message, from_email, [superuser_email], html_message=html_message)

    return redirect('message:books')
def error_page(request):
    return HttpResponseBadRequest("Payment is already approved.")


def calculate_refund_amount(booking):
    # Assume refund policy is based on the number of days between booking and current date
    refund_policy = {
        0: Decimal('0.5'),  # Refund 50% if cancelled on the same day as booking
        1: Decimal('0.75'),  # Refund 75% if cancelled within 1 day of booking
        2: Decimal('0.9'),  # Refund 90% if cancelled within 2 days of booking
        # Add more refund policies as needed
    }
    
    # Calculate the number of days between booking date and current date
    booking_date = booking.booking_date.date()  # Convert to datetime.date object
    current_date = datetime.now().date()
    days_difference = (current_date - booking_date).days
    
    # Determine the refund percentage based on the number of days difference
    refund_percentage = refund_policy.get(days_difference, Decimal('1.0'))  # Default to full refund if no matching policy found
    
    # Calculate refund amount based on the total amount paid for the booking
    total_price = booking.total_price
    
    # Convert total_price to Decimal for compatibility
    total_price_decimal = Decimal(str(total_price))
    
    refund_amount = total_price_decimal * refund_percentage
    
    return refund_amount


def cancel_bookings(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        
        # Calculate refund amount
        refund_amount = calculate_refund_amount(booking)
        
        # Update booking status and payment status
        booking.booking_status = 'cancelled'
        booking.payment_status = 'refunded'
        booking.save()
        
        # Update refund amount in booking object (optional)
        booking.refund_amount = refund_amount
        booking.save()
        
        messages.success(request, f"Booking cancelled and refunded successfully. Refund amount: {refund_amount}")
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found.")
    
    return redirect('all_bookings')


def send_email_notification(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    subject = 'Booking Acceptance Notification'
    html_message = render_to_string('payment/email_accept_notification.html', {
        'booking': booking,
        'house_address': booking.house.address if booking.house else 'N/A',
    })
    plain_message = strip_tags(html_message)
    from_email = 'fikefiresew1234@gmail.com'

    # Get superuser email
    superuser_email = User.objects.filter(is_superuser=True).first().email

    send_mail(subject, plain_message, from_email, [superuser_email], html_message=html_message)
    return redirect('message:books')





def submit_tenant_info(request):
    if request.method == 'POST':
        form = TenantInfoForm(request.POST, request.FILES)
        if form.is_valid():
            booking_id = request.POST.get('booking_id')
            booking = Booking.objects.get(id=booking_id)
            booking.id_document = form.cleaned_data['id_document']
            booking.tenant_photo = form.cleaned_data['tenant_photo']
            booking.save()
            return redirect('payment-success')  # Redirect to payment success page
    else:
        form = TenantInfoForm()
    return render(request, 'submit_tenant_info.html', {'form': form})

def PaymentSuccessful(request, product_id):
    product = Listing.objects.get(id=product_id)
    return render(request, 'payment/payment-success.html', {'product': product})

def paymentFailed(request, product_id):
    product = Listing.objects.get(id=product_id)
    return render(request, 'payment/payment-failed.html', {'product': product})

def paymentpage(request, product_id):
    product = Listing.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'payment/paymentpage.html', context)

def mark_notification_as_seen(request, id):
    # Get the notification by ID
    notification = Notification.objects.get(id=id)
    
    # Mark the notification as seen
    notification.seen = True
    notification.save()
    if 'unseen_count' in request.session:
        request.session['unseen_count'] = max(0, request.session.get('unseen_count', 0) - 1)

    return redirect('poster')

def poster(request):
    if request.method=='POST':
        message=request.POST.get('message')
        notification=Notification(message=message)
        notification.save()
    notifications = Notification.objects.all()
    unseen_count = Notification.objects.filter(seen=False).count()
    return render(request,'payment/writenotification.html',{'notifications':notifications,
                                                   'unseen_count':unseen_count})


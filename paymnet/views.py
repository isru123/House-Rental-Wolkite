# from django.shortcuts import render
# from main.models import Listing
# from .models import Payment

# from .models import Notification
# from django.shortcuts import redirect

# # Your code where you use redirect...

# from paypal.standard.forms import PayPalPaymentsForm
# from django.conf import settings
# import uuid
# from django.urls import reverse

# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from .models import Booking
# from main.models import Listing,Upload
# from paypal.standard.forms import PayPalPaymentsForm
# import uuid



# @login_required
# def CheckOut(request, product_id):
#     product = Listing.objects.get(id=product_id)
#     host = request.get_host()

#     # Generate a UUID for the payment ID
#     payment_id = uuid.uuid4().hex

#     # Get the seller's user object
#     recipient_user = product.seller.user  # Assuming the seller is associated with a user

#     # Save payment information to the database
#     payment = Payment.objects.create(
#         amount=product.price,
#         payer=request.user,
#         recipient=recipient_user,
#         payment_id=payment_id,
#     )

#     # Fetch tenant's document and photo
#     tenant_uploads = Upload.objects.filter(tenant=request.user.profile)

#     # Assuming you want to use the first upload found
#     if tenant_uploads.exists():
#         tenant_upload = tenant_uploads.first()
#         id_document_url = tenant_upload.document.url
#         tenant_photo_url = tenant_upload.photo.url
#     else:
#         # Handle the case when no upload is found for the tenant
#         id_document_url = ''  # Provide a default value or raise an error
#         tenant_photo_url = ''  # Provide a default value or raise an error

#     # Create a booking object
#     booking = Booking.objects.create(
#         tenant=request.user,
#         house=product,
#         total_price=product.price,
#         booking_status='pending',
#         payment_status='pending',
#         confirmation_code=uuid.uuid4().hex,
#         payment_id=payment_id,  # Use the generated payment_id
#         id_document=id_document_url,
#         tenant_photo=tenant_photo_url,
#     )

#     paypal_checkout = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': product.price,
#         'invoice': payment_id,  # Pass the generated payment ID to PayPal
#         'currency_code': 'USD',
#         'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#         'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
#         'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
#     }

#     paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#     context = {
#         'product': product,
#         'paypal': paypal_payment
#     }

#     return render(request, 'payment/checkout.html', context)
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.http import HttpResponseBadRequest
# from django.http import HttpResponse

# @user_passes_test(lambda u: u.is_superuser)
# def approve_payment(request, booking_id):
#     # Get the booking object
#     booking = get_object_or_404(Booking, id=booking_id)
    
#     if booking.payment_status != 'pending':
#         return HttpResponseBadRequest("Payment is already approved.")
    
#     # Mark payment as paid
#     booking.payment_status = 'paid'
#     booking.save()

#     # Redirect back to the admin page
#     return redirect('admin:paymnet_booking_changelist')
# def confirm_booking(request, booking_id):
#     # Get the booking object
#     booking = Booking.objects.get(id=booking_id)
#     # Confirm the booking (update booking_status)
#     booking.booking_status = 'confirmed'
#     booking.save()
#     return redirect('admin:paymnet_booking_changelist')  # Redirect to booking list in admin

# def change_booking_status(request, booking_id, new_status):
#     # Get the booking object
#     booking = Booking.objects.get(id=booking_id)
#     # Update booking_status
#     booking.booking_status = new_status
#     booking.save()
#     return redirect('admin:paymnet_booking_changelist') 
# # views.py

# from django.shortcuts import get_object_or_404, redirect
# from .models import Booking

# # views.py

# from django.shortcuts import get_object_or_404, redirect
# from .models import Booking

# def cancel_booking(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     if request.method == 'POST':
#         # Update the booking status to 'canceled'
#         booking.booking_status = 'canceled'
#         booking.save()
#         return redirect('admin:paymnet_booking_changelist')  # Redirect to the booking change list in admin
#     return render(request, 'payment/cancel_booking_confirm.html', {'booking': booking})

# from django.shortcuts import render

# def error_page(request):
#         return HttpResponseBadRequest("Payment is already approved.")

# # def CheckOut(request, product_id):
# #     product = Listing.objects.get(id=product_id)
# #     host = request.get_host()

# #     # Generate a UUID for the payment ID
# #     payment_id = uuid.uuid4().hex

# #     # Get the seller's user object
# #     recipient_user = product.seller.user  # Assuming the seller is associated with a user

# #     # Save payment information to the database
# #     payment = Payment.objects.create(
# #         amount=product.price,
# #         payer=request.user,
# #         recipient=recipient_user,
# #         payment_id=payment_id,
# #     )

# #     # Create a booking object
# #     booking = Booking.objects.create(
# #         tenant=request.user,
# #         house=product,
# #         total_price=product.price,
# #         booking_status='pending',
# #         payment_status='pending',
# #         confirmation_code=uuid.uuid4().hex,
# #         payment_id=payment_id,  # Use the generated payment_id
# #         id_document='',  # Add appropriate values
# #         tenant_photo='',  # Add appropriate values
# #     )

# #     paypal_checkout = {
# #         'business': settings.PAYPAL_RECEIVER_EMAIL,
# #         'amount': product.price,
# #         'invoice': payment_id,  # Pass the generated payment ID to PayPal
# #         'currency_code': 'USD',
# #         'notify_url': f"http://{host}{reverse('paypal-ipn')}",
# #         'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
# #         'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
# #     }

# #     paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

# #     context = {
# #         'product': product,
# #         'paypal': paypal_payment
# #     }

# #     return render(request, 'payment/checkout.html', context)
# # from .forms import TenantInfoForm

# # @login_required
# # def CheckOut(request, product_id):
# #     if request.method == 'POST':
# #         form = TenantInfoForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             product = Listing.objects.get(id=product_id)
# #             host = request.get_host()

# #             # Generate a UUID for the payment ID
# #             payment_id = uuid.uuid4().hex

# #             # Get the seller's user object
# #             recipient_user = product.seller.user  # Assuming the seller is associated with a user

# #             # Save payment information to the database
# #             payment = Payment.objects.create(
# #                 amount=product.price,
# #                 payer=request.user,
# #                 recipient=recipient_user,
# #                 payment_id=payment_id,
# #             )

# #             # Create a booking object
# #             booking = Booking.objects.create(
# #                 tenant=request.user,
# #                 house=product,
# #                 total_price=product.price,
# #                 booking_status='pending',
# #                 payment_status='pending',
# #                 confirmation_code=uuid.uuid4().hex,
# #                 payment_id=payment_id,  # Use the generated payment_id
# #                 id_document=form.cleaned_data['id_document'],
# #                 tenant_photo=form.cleaned_data['tenant_photo'],
# #             )

# #             paypal_checkout = {
# #                 'business': settings.PAYPAL_RECEIVER_EMAIL,
# #                 'amount': product.price,
# #                 'invoice': payment_id,  # Pass the generated payment ID to PayPal
# #                 'currency_code': 'USD',
# #                 'notify_url': f"http://{host}{reverse('paypal-ipn')}",
# #                 'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
# #                 'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
# #             }

# #             paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

# #             context = {
# #                 'product': product,
# #                 'paypal': paypal_payment
# #             }

# #             return render(request, 'payment/checkout.html', context)
# #     else:
# #         form = TenantInfoForm()  # Create an empty form for GET requests

# #     return render(request, 'payment/checkout.html', {'form': form})

# from .forms import TenantInfoForm
# from .models import Booking
# def submit_tenant_info(request):
#     if request.method == 'POST':
#         form = TenantInfoForm(request.POST, request.FILES)
#         if form.is_valid():
#             booking_id = request.POST.get('booking_id')
#             booking = Booking.objects.get(id=booking_id)
#             booking.id_document = form.cleaned_data['id_document']
#             booking.tenant_photo = form.cleaned_data['tenant_photo']
#             booking.save()
#             return redirect('payment-success')  # Redirect to payment success page
#     else:
#         form = TenantInfoForm()
#     return render(request, 'submit_tenant_info.html', {'form': form})


# def PaymentSuccessful(request, product_id):

#     product = Listing.objects.get(id=product_id)

#     return render(request, 'payment/payment-success.html', {'product': product})

# def paymentFailed(request, product_id):

#     product = Listing.objects.get(id=product_id)

#     return render(request, 'payment/payment-failed.html', {'product': product})


# def paymentpage(request, product_id):
#     product = Listing.objects.get(id=product_id)
#     context = {
#         'product': product
#     }
#     return render(request, 'payment/paymentpage.html', context)

# def mark_notification_as_seen(request, id):
#     # Get the notification by ID
#     notification = Notification.objects.get(id=id)
    
#     # Mark the notification as seen
#     notification.seen = True
#     notification.save()
#     if 'unseen_count' in request.session:
#         request.session['unseen_count'] = max(0, request.session.get('unseen_count', 0) - 1)

#     return redirect('poster')

# def poster(request):
#     if request.method=='POST':
#         message=request.POST.get('message')
#         notification=Notification(message=message)
#         notification.save()
#     notifications = Notification.objects.all()
#     unseen_count = Notification.objects.filter(seen=False).count()
#     return render(request,'payment/writenotification.html',{'notifications':notifications,
#                                                    'unseen_count':unseen_count})


from .models import Payment

from .models import Notification
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Booking
from main.models import Listing, Upload
from .forms import TenantInfoForm

from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import transaction

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
@login_required
# def CheckOut(request, product_id):
#     product = Listing.objects.get(id=product_id)
#     host = request.get_host()

#     # Generate a UUID for the payment ID
#     payment_id = uuid.uuid4().hex

#     # Get the seller's user object
#     recipient_user = product.seller.user  # Assuming the seller is associated with a user

#     # Save payment information to the database
#     payment = Payment.objects.create(
#         amount=product.price,
#         payer=request.user,
#         recipient=recipient_user,
#         payment_id=payment_id,
#     )

#     # Create a booking object
#     booking = Booking.objects.create(
#         tenant=request.user,
#         house_id=product.id,
#         house=product,

#         total_price=product.price,
#         booking_status='pending',
#         payment_status='pending', 
#         confirmation_code=uuid.uuid4().hex,
#         payment_id=payment_id,  # Use the generated payment_id
#         id_document='',  # Add appropriate values
#         tenant_photo='',  # Add appropriate values
#     )

#     # Send email notification to seller
#     subject = 'Payment Received'
#     html_message = render_to_string('payment/email_payment_notification.html', {'product': product})
#     plain_message = strip_tags(html_message)
#     from_email = 'fikefiresew1234@gmail.com'  # Update with your email address
#     to_email = product.seller.user.email
#     send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

#     paypal_checkout = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': product.price,
#         'invoice': payment_id,  # Pass the generated payment ID to PayPal
#         'currency_code': 'USD',
#         'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#         'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
#         'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
#     }

#     paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#     context = {
#         'product': product,
#         'paypal': paypal_payment
#     }

#     return render(request, 'payment/checkout.html', context)


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
        id_document='',
        tenant_photo='',
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


# def CheckOut(request, product_id):
#     try:
#         product = Listing.objects.get(id=product_id)
#         host = request.get_host()

#         # Check if a payment with the same payment ID exists and it's paid
#         existing_payment = Booking.objects.filter(payment_id=product_id, payment_status='paid').exists()
#         if existing_payment:
#             # If a paid payment with the same ID exists, prevent further payment
#             messages.error(request, "You've already paid for this product.")
#             return redirect('payment-error')

#         # Calculate system fee (0.2% of the product price)
#         system_fee = round((0.2 / 100) * product.price, 2)

#         # Calculate total price including system fee
#         total_price = round(product.price + system_fee, 2)

#         # Generate a UUID for the payment ID
#         payment_id = uuid.uuid4().hex

#         # Save payment information to the database
#         payment = Payment.objects.create(
#             amount=total_price,
#             payer=request.user,
#             recipient=product.seller.user,
#             payment_id=payment_id,
#         )

#         # Create a booking object
#         booking = Booking.objects.create(
#             tenant=request.user,
#             house_id=product.id,
#             house=product,
#             total_price=total_price,
#             booking_status='pending',
#             payment_status='pending',
#             confirmation_code=uuid.uuid4().hex,
#             payment_id=payment_id,
#             id_document='',
#             tenant_photo='',
#         )

#         # Send email notification to seller
#         subject = 'Payment Received'
#         html_message = render_to_string('payment/email_payment_notification.html', {'product': product})
#         plain_message = strip_tags(html_message)
#         from_email = 'fikefiresew1234@gmail.com'
#         to_email = product.seller.user.email
#         send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

#         # PayPal checkout parameters
#         paypal_checkout = {
#             'business': settings.PAYPAL_RECEIVER_EMAIL,
#             'amount': "{:.2f}".format(total_price),
#             'invoice': payment_id,
#             'currency_code': 'USD',
#             'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#             'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
#             'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
#         }

#         # Create PayPalPaymentsForm
#         paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#         context = {
#             'product': product,
#             'paypal': paypal_payment,
#             'system_fee': "{:.2f}".format(system_fee),
#             'total_price': "{:.2f}".format(total_price)
#         }

#         return render(request, 'payment/checkout.html', context)
#     except Exception as e:
#         # Print the exception message for debugging
#         print(e)
#         # Return to the error page with the exception message
#         return render(request, 'payment/error.html', {'error_message': str(e)})

from django.contrib.auth.models import User



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

    return redirect('books')

# def cancel_bookings(request, booking_id):
#     try:
#         booking = Booking.objects.get(id=booking_id)
#         booking.booking_status = 'cancelled'
#         booking.payment_status = 'refunded'
#         booking.save()
#         messages.success(request, "Booking cancelled and refunded successfully.")
#     except Booking.DoesNotExist:
#         messages.error(request, "Booking not found.")
   
#     return redirect('admin:paymnet_booking_changelist')  # Redirect to wherever you want
from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect
from .models import Booking  # Import your Booking model

from django.utils import timezone

from decimal import Decimal

# def calculate_refund_amount(booking):
#     # Convert total_price to float
#     total_price_float = float(booking.total_price)
    
#     # Calculate refund amount based on booking criteria
#     if total_price_float > 1000:
#         # Refund 70% of the total price for bookings with a total price greater than 1000
#         return Decimal(total_price_float * 0.7)
#     elif total_price_float > 500:
#         # Refund 50% of the total price for bookings with a total price greater than 500
#         return Decimal(total_price_float * 0.5)
#     else:
#         # Refund 30% of the total price for bookings with a total price less than or equal to 500
#         return Decimal(total_price_float * 0.3)
from datetime import timedelta

from datetime import timedelta

# def calculate_refund_amount(booking):
#     # Convert total_price to float
#     total_price_float = float(booking.total_price)

#     # Calculate time difference between booking date and current datetime
#     time_difference = booking.booking_date - timezone.now()

#     seconds_difference = time_difference.total_seconds()

#     print("Seconds before booking:", seconds_difference)

#     # Define refund policy based on the time elapsed since booking
#     if seconds_difference <= 60:  # Within 1 minute after booking
#         return Decimal(total_price_float * 0.8)  # For example, 10% refund
#     elif seconds_difference <= 120:  # Within 2 minutes after booking
#         return Decimal(total_price_float * 0.5)  # For example, 20% refund
#     elif seconds_difference <= 180:  # Within 3 minutes after booking
#         return Decimal(total_price_float * 0.3)  # For example, 30% refund
#     elif seconds_difference <= 3600:  # Within 1 hour after booking
#         return Decimal(total_price_float * 0.5)  # For example, 50% refund
#     else:
#         # No refund if cancellation is made later than the specified time frame
#         return Decimal(0)
from datetime import datetime

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
    return redirect('books')  # Redirect to the booking history page after sending the email
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def display_all_bookings(request):
    # Fetch all bookings from the database
    bookings = Booking.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(bookings, 10)
    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        bookings = paginator.page(1)
    except EmptyPage:
        bookings = paginator.page(paginator.num_pages)
    
    # Render the template with bookings data
    return render(request, 'adminApp/manage-owner-task.html', {'bookings': bookings})

def display_all_payments(request):
    # Fetch all bookings from the database
    bookings = Booking.objects.all()
    all_payments = Payment.objects.all()
    all_bookings = Booking.objects.all()

    context = {
        'bookings': bookings,

        'all_payments': all_payments,
        'all_bookings': all_bookings
    }

    
    return render(request, 'adminApp/paymenthistory.html', context)    
# @login_required
# def CheckOut(request, product_id):
#     product = Listing.objects.get(id=product_id)
#     host = request.get_host()

#     # Generate a UUID for the payment ID
#     payment_id = uuid.uuid4().hex

#     # Get the seller's user object
#     recipient_user = product.seller.user  # Assuming the seller is associated with a user

#     # Save payment information to the database
#     payment = Payment.objects.create(
#         amount=product.price,
#         payer=request.user,
#         recipient=recipient_user,
#         payment_id=payment_id,
#     )

#     # Create a booking object
#     booking = Booking.objects.create(
#         tenant=request.user,
#         house=product,
#         total_price=product.price,
#         booking_status='pending',
#         payment_status='pending',
#         confirmation_code=uuid.uuid4().hex,
#         payment_id=payment_id,  # Use the generated payment_id
#         id_document='',  # Add appropriate values
#         tenant_photo='',  # Add appropriate values
#     )

#     paypal_checkout = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': product.price,
#         'invoice': payment_id,  # Pass the generated payment ID to PayPal
#         'currency_code': 'USD',
#         'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#         'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
#         'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
#     }

#     paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#     context = {
#         'product': product,
#         'paypal': paypal_payment
#     }

#     return render(request, 'payment/checkout.html', context)

@user_passes_test(lambda u: u.is_superuser)
def approve_payment(request, booking_id):
    # Get the booking object
    booking = get_object_or_404(Booking, id=booking_id)
    
    if booking.payment_status == 'pending':
        # Mark payment as paid
        booking.payment_status = 'paid'
        booking.save()
    
    # Redirect back to the admin page regardless of payment status
    return redirect('all_bookings')

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
    return redirect('all_bookings')  # Redirect to booking list in admin

def change_booking_status(request, booking_id, new_status):
    # Get the booking object
    booking = Booking.objects.get(id=booking_id)
    # Update booking_status
    booking.booking_status = new_status
    booking.save()
    return redirect('all_bookings') 

# def cancel_booking(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     if request.method == 'POST':
#         # Update the booking status to 'canceled'
#         booking.booking_status = 'canceled'
#         booking.save()
#         return redirect('admin:paymnet_booking_changelist')  # Redirect to the booking change list in admin
#     return redirect('admin:paymnet_booking_changelist')  # Redirect to the booking change list in admin

def error_page(request):
    return HttpResponseBadRequest("Payment is already approved.")

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

# def paymentpage(request, product_id):
#     product = Listing.objects.get(id=product_id)
#     context = {
#         'product': product
#     }
#     return render(request, 'payment/paymentpage.html', context)
from django.http import HttpResponse

from .models import Payment

def paymentpage(request, product_id):
    product = Listing.objects.get(id=product_id)
    
    # Check if there's an existing payment for this listing
    existing_payment = Payment.objects.filter(recipient=request.user, payment_id=product_id).exists()
    if existing_payment:
        # Handle case where payment already exists for this listing
        # For example, redirect the user to a page indicating they've already paid
        return HttpResponse("You've already paid for this listing.")
    else:
        # Proceed with the payment process
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


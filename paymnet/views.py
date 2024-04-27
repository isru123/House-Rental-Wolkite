from django.shortcuts import render
from main.models import Listing
from .models import Payment

from .models import Notification
from django.shortcuts import redirect

# Your code where you use redirect...

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Booking
from main.models import Listing
from paypal.standard.forms import PayPalPaymentsForm
import uuid

@login_required
def CheckOut(request, product_id):
    product = Listing.objects.get(id=product_id)
    host = request.get_host()

    # Generate a UUID for the payment ID
    payment_id = uuid.uuid4().hex

    # Get the seller's user object
    recipient_user = product.seller.user  # Assuming the seller is associated with a user

    # Save payment information to the database
    payment = Payment.objects.create(
        amount=product.price,
        payer=request.user,
        recipient=recipient_user,
        payment_id=payment_id,
    )

    # Create a booking object
    booking = Booking.objects.create(
        tenant=request.user,
        house=product,
        total_price=product.price,
        booking_status='pending',
        payment_status='pending',
        confirmation_code=uuid.uuid4().hex,
        payment_id=payment_id,  # Use the generated payment_id
        id_document='',  # Add appropriate values
        tenant_photo='',  # Add appropriate values
    )

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'invoice': payment_id,  # Pass the generated payment ID to PayPal
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': product,
        'paypal': paypal_payment
    }

    return render(request, 'payment/checkout.html', context)
# from .forms import TenantInfoForm

# @login_required
# def CheckOut(request, product_id):
#     if request.method == 'POST':
#         form = TenantInfoForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = Listing.objects.get(id=product_id)
#             host = request.get_host()

#             # Generate a UUID for the payment ID
#             payment_id = uuid.uuid4().hex

#             # Get the seller's user object
#             recipient_user = product.seller.user  # Assuming the seller is associated with a user

#             # Save payment information to the database
#             payment = Payment.objects.create(
#                 amount=product.price,
#                 payer=request.user,
#                 recipient=recipient_user,
#                 payment_id=payment_id,
#             )

#             # Create a booking object
#             booking = Booking.objects.create(
#                 tenant=request.user,
#                 house=product,
#                 total_price=product.price,
#                 booking_status='pending',
#                 payment_status='pending',
#                 confirmation_code=uuid.uuid4().hex,
#                 payment_id=payment_id,  # Use the generated payment_id
#                 id_document=form.cleaned_data['id_document'],
#                 tenant_photo=form.cleaned_data['tenant_photo'],
#             )

#             paypal_checkout = {
#                 'business': settings.PAYPAL_RECEIVER_EMAIL,
#                 'amount': product.price,
#                 'invoice': payment_id,  # Pass the generated payment ID to PayPal
#                 'currency_code': 'USD',
#                 'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#                 'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
#                 'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
#             }

#             paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#             context = {
#                 'product': product,
#                 'paypal': paypal_payment
#             }

#             return render(request, 'payment/checkout.html', context)
#     else:
#         form = TenantInfoForm()  # Create an empty form for GET requests

#     return render(request, 'payment/checkout.html', {'form': form})

from .forms import TenantInfoForm
from .models import Booking
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





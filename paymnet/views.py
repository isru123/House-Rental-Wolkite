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
        house_id=product.id,
        house=product,

        total_price=product.price,
        booking_status='pending',
        payment_status='pending',
        confirmation_code=uuid.uuid4().hex,
        payment_id=payment_id,  # Use the generated payment_id
        id_document='',  # Add appropriate values
        tenant_photo='',  # Add appropriate values
    )

    # Send email notification to seller
    subject = 'Payment Received'
    html_message = render_to_string('payment/email_payment_notification.html', {'product': product})
    plain_message = strip_tags(html_message)
    from_email = 'fikefiresew1234@gmail.com'  # Update with your email address
    to_email = product.seller.user.email
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

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
    return redirect('admin:paymnet_booking_changelist')

def confirm_booking(request, booking_id):
    # Get the booking object
    booking = Booking.objects.get(id=booking_id)
    # Confirm the booking (update booking_status)
    booking.booking_status = 'confirmed'
    booking.save()
    return redirect('admin:paymnet_booking_changelist')  # Redirect to booking list in admin

def change_booking_status(request, booking_id, new_status):
    # Get the booking object
    booking = Booking.objects.get(id=booking_id)
    # Update booking_status
    booking.booking_status = new_status
    booking.save()
    return redirect('admin:paymnet_booking_changelist') 

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        # Update the booking status to 'canceled'
        booking.booking_status = 'canceled'
        booking.save()
        return redirect('admin:paymnet_booking_changelist')  # Redirect to the booking change list in admin
    return redirect('admin:paymnet_booking_changelist')  # Redirect to the booking change list in admin

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


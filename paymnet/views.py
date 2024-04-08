from django.shortcuts import render
from main.models import Listing
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse


# import paypalrestsdk
# import uuid
# from django.urls import reverse
# from django.conf import settings
# from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm
# import requests
# import json
# import uuid
# from django.urls import reverse
# from django.conf import settings
# from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm



# def CheckOut(request, product_id):
#     product = Listing.objects.get(id=product_id)
#     host = request.get_host()

#     paypal_checkout = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': product.price,
#         'invoice': uuid.uuid4(),
#         'currency_code': 'USD',
#         'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#         'return_url': f"http://{host}{reverse('payment-success', kwargs={'product_id': product.id})}",
#         'cancel_url': f"http://{host}{reverse('payment-failed', kwargs={'product_id': product.id})}",
#     }

#     paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#     # Set up the PayPal API credentials
#     client_id = 'AVbpsVA6kHOYNmFF-d_OH7G1Dl0FlQ8muRgw5tEGMuoZHCavFkzQQRGWncp4Df6Ih9ef_4F_GiLsylLf'
#     client_secret = 'EBogCHN5AUEzmx0K3Ws2e_kNEJHulGRUrlhNPqzpJ2rlfv7fs653Vx-Pt-PE2fENfws6e3l06Lif0HlD'

#     # Generate an access token
#     auth_url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
#     data = {'grant_type': 'client_credentials'}
#     response = requests.post(auth_url, data=data, auth=(client_id, client_secret))
#     try:
#         access_token = json.loads(response.text)['access_token']
#     except KeyError:
#         error_message = "Failed to retrieve access token from PayPal API."
#         context = {
#             'product': product,
#             'error_message': error_message
#         }
#         return render(request, 'payment/payment-failed.html', context)

#     # Make a request to retrieve the balance
#     balance_url = 'https://api.sandbox.paypal.com/v1/payments/balance'
#     headers = {'Authorization': f'Bearer {access_token}'}
#     response = requests.get(balance_url, headers=headers)
#     try:
#         balance_data = json.loads(response.text)
#         account_balance = balance_data['available'][0]['amount']
#     except (KeyError, json.JSONDecodeError):
#         error_message = "Failed to retrieve account balance from PayPal API."
#         context = {
#             'product': product,
#             'error_message': error_message
#         }
#         return render(request, 'payment/payment-failed.html', context)

#     if float(account_balance) < product.price:
#         message = "Sorry, you do not have enough funds in your PayPal account to complete the payment."
#         context = {
#             'product': product,
#             'message': message
#         }
#     else:
#         context = {
#             'product': product,
#             'paypal': paypal_payment
#         }

#     return render(request, 'payment/checkout.html', context)




def CheckOut(request, product_id):

    product = Listing.objects.get(id=product_id)

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'product_id': product.id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'product_id': product.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': product,
        'paypal': paypal_payment
    }

    return render(request, 'payment/checkout.html', context)






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







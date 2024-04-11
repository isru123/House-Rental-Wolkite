from django.urls import path
from . import views

urlpatterns = [
    
   path('paymentpage/<uuid:product_id>/', views.paymentpage, name='product-view'),

    path('checkout/<uuid:product_id>/', views.CheckOut, name='checkout'),
    path('payment-success/<uuid:product_id>/', views.PaymentSuccessful, name='payment-success'),

    path('payment-failed/<uuid:product_id>/', views.paymentFailed, name='payment-failed'),

]
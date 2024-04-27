from django.urls import path
from . import views 

urlpatterns = [
    
   path('paymentpage/<uuid:product_id>/', views.paymentpage, name='product-view'),

    path('checkout/<uuid:product_id>/', views.CheckOut, name='checkout'),
    path('payment-success/<uuid:product_id>/', views.PaymentSuccessful, name='payment-success'),

    path('payment-failed/<uuid:product_id>/', views.paymentFailed, name='payment-failed'),
  path('mark-notification/<int:id>/', views.mark_notification_as_seen, name='mark_notification_as_seen'),
    path('poster/', views.poster, name='poster'),
    path('submit-tenant-info/', views.submit_tenant_info, name='submit_tenant_info'),

]
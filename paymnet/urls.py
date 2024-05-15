from django.urls import path
from . import views 

urlpatterns = [
    
    path('paymentpage/<uuid:product_id>/', views.paymentpage, name='product-view'),

    path('checkout/<uuid:product_id>/', views.CheckOut, name='checkout'),
    path('payment-success/<uuid:product_id>/', views.PaymentSuccessful, name='payment-success'),
    path('approve_payment/<uuid:booking_id>/', views.approve_payment, name='approve_payment'),
    path('change-booking-status/<uuid:booking_id>/<str:new_status>/', views.change_booking_status, name='change_booking_status'),
    path('error/', views.error_page, name='error_page'),
    path('payment-failed/<uuid:product_id>/', views.paymentFailed, name='payment-failed'),
    path('mark-notification/<int:id>/', views.mark_notification_as_seen, name='mark_notification_as_seen'),
    path('poster/', views.poster, name='poster'),
    path('submit-tenant-info/', views.submit_tenant_info, name='submit_tenant_info'),
    path('confirm-booking/<uuid:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('cancel-booking/<uuid:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('cancel-bookings/<uuid:booking_id>/', views.cancel_bookings, name='cancel_bookings'),
<<<<<<< HEAD
path('send-email-notification/<uuid:booking_id>/', views.send_email_notification, name='send_email_notification'),
    path('all-bookings/', views.display_all_bookings, name='all_bookings'),
        path('all-payments/', views.display_all_payments, name='display_all_payments'),


=======
    path('send-email-notification/<uuid:booking_id>/', views.send_email_notification, name='send_email_notification'),
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9
]
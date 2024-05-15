from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Notification, Payment, Booking

admin.site.register(Notification)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

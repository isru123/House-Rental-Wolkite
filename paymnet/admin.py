from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Notification, Payment, Booking

admin.site.register(Notification)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'amount', 'payer', 'recipient', 'timestamp']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'tenant', 'house', 'total_price', 'booking_status', 'payment_status', 'confirmation_code', 'approve_button', 'change_status_button']
    # actions = ['approve_payment']

    # def approve_button(self, obj):
    #     approve_payment_url = reverse('approve_payment', args=[obj.id])

    #     if obj.booking_status == 'confirmed':
    #         return format_html('<a class="button" href="{}">Approve Payment</a>', approve_payment_url)
    #     else:
    #         approve_payment_url = reverse('approve_payment', args=[obj.id])
    #         return format_html('<a class="button" href="{}">Approve Payment</a>', approve_payment_url)
    # approve_button.short_description = "Approve Payment"

    # def approve_button_description(self, obj):
    #     if obj.booking_status == 'confirmed':
    #         return format_html('<button type="button" class="button button-green" onclick="window.location=\'{}\'">Confirmed</button>', reverse('confirm_booking', args=[obj.id]))

    #     else:
    #         approve_payment_url = reverse('approve_payment', args=[obj.id])
    #         return format_html('<a class="button" href="{}">Approve Payment</a>', approve_payment_url)

    # def change_status_button(self, obj):
    #     if obj.booking_status == 'pending':
    #         return format_html('<a class="button" href="{}">Confirm Booking</a>', reverse('confirm_booking', args=[obj.id]))
    #     elif obj.booking_status == 'confirmed':
    #         return format_html('<a class="button" href="{}">Cancel Booking</a>', reverse('cancel_booking', args=[obj.id]))
    #     else:
    #         return ''  # Return an empty string for other statuses
    # change_status_button.short_description = "Change Booking Status"

    # def approve_payment(self, request, queryset):
    #     for booking in queryset:
    #         # Send a request to approve_payment URL with booking_id
    #         approve_payment_url = reverse('approve_payment', args=[booking.id])
    #         # You can customize the HTML as needed for the action display
    #         message = format_html('<a class="button" href="{}">Approve Payment</a>', approve_payment_url)
    #         self.message_user(request, message)
    # approve_payment.short_description = "Approve selected bookings"

    # # Set the short description for the approve button dynamically
    # approve_button_description.short_description = "Approve Payment"

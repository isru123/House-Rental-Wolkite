from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Booking,Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['id', 'amount', 'payer', 'recipient', 'timestamp']
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tenant', 'house', 'total_price', 'refund_amount', 'get_booking_status', 'get_payment_status', 'confirmation_code', 'confirm_button', 'cancel_button', 'approve_button']

    def get_booking_status(self, obj):
        # Replace this with your logic to get booking status
        return obj.booking_status
    
    def get_payment_status(self, obj):
        # Replace this with your logic to get payment status
        return obj.payment_status

    def confirm_button(self, obj):
        if obj.booking_status == 'pending':
            return format_html('<a class="button" href="{}">Confirm Booking</a>',
                               reverse('confirm_booking', args=[obj.id]))
        else:
            return ""
    confirm_button.short_description = "Confirm"

    def cancel_button(self, obj):
        if obj.booking_status == 'pending':
            
            return format_html('<a class="button" href="{}">Cancel Booking</a>',
                               reverse('cancel_bookings', args=[obj.id]))
        else:
            return ""
    cancel_button.short_description = "Cancel"

    def approve_button(self, obj):
        if obj.payment_status == 'pending':
            approve_payment_url = reverse('approve_payment', args=[obj.id])
            return format_html('<a class="button" href="{}">Approve Payment</a>', approve_payment_url)
        else:
            return ""
    approve_button.short_description = "Approve Payment"

    def change_status_button(self, obj):
        if obj.booking_status == 'pending':
            return format_html('<a class="button" href="{}">Confirm Booking</a>', reverse('confirm_booking', args=[obj.id]))
        elif obj.booking_status == 'pending':
            return format_html('<a class="button" href="{}">Cancel Booking</a>', reverse('cancel_bookings', args=[obj.id]))
        else:
            return ''  # Return an empty string for other statuses
    change_status_button.short_description = "Change Booking Status"

    def approve_payment(self, request, queryset):
        for booking in queryset:
            if booking.payment_status == 'pending':
                # Send a request to approve_payment URL with booking_id
                approve_payment_url = reverse('approve_payment', args=[booking.id])
                # You can customize the HTML as needed for the action display
                message = format_html('<a class="button" href="{}">Approve Payment</a>', approve_payment_url)
                self.message_user(request, message)
            else:
                self.message_user(request, "Payment already approved for selected bookings.")

    approve_payment.short_description = "Approve selected bookings"
=======
    pass
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

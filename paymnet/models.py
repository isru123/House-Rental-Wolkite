from django.db import models
from main.models import Listing

from django.utils import timezone
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Notification(models.Model):
    message = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def str(self):
        return self.message

        


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payer = models.ForeignKey(User, related_name='payments_made', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='payments_received', on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Payment {self.id} - Amount: ${self.amount}"        



class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_as_tenant')
    house = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    listing_id = models.UUIDField(null=True, blank=True, editable=False)  # Added field for listing ID
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    confirmation_code = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=100)  # Assuming payment_id is used to store payment information
<<<<<<< HEAD
    id_document = models.FileField(upload_to='tenant_documents/')
    tenant_photo = models.FileField(upload_to='tenant_photos/')
    booking_date = models.DateTimeField()  # Add a field for booking date and time
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Added refund_amount field
    paypal_transaction_id = models.CharField(max_length=100, null=True, blank=True)
=======
 
    booking_date = models.DateTimeField()  # Add a field for booking date and time
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Added refund_amount field
   
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

    def save(self, *args, **kwargs):
        if self.house:
            self.listing_id = self.house.id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking ID: {self.id}, Tenant: {self.tenant.username}, House: {self.house.address}"
    
    
    
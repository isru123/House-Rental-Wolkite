from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField
import random
from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
  
    
    def __str__(self):
        return f'Location {self.id}'
    
     
    
class Profile(models.Model):
      USER_TYPES = [
        ('Public', 'Public'),
        ('Owner','Owner'),
        ('Admin', 'Admin'),
    ]
      user = models.OneToOneField(User, on_delete = models.CASCADE)
      photo = models.ImageField(upload_to= user_directory_path ,null=True)
      bio = models.CharField(max_length=140, blank=True)
      address = models.TextField()
      contact_No = models.IntegerField()
      userType = models.CharField(max_length=10, choices=USER_TYPES, default='Public')
      verified = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      location = models.OneToOneField(Location, on_delete = models.SET_NULL, null=True)
    
    
    
    
      def __str__(self):
          return f'{self.user.username}\'s Profile'





# class UserProfile(models.Model):

#     USER_TYPES = [
#         ('Public', 'Public'),
#         ('Owner','Owner'),
#         ('Admin', 'Admin'),
#     ]
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     profilePicture = models.ImageField(blank=True, null=True)
#     address = models.TextField()
#     contact_No = models.IntegerField()
#     userType = models.CharField(max_length=10, choices=USER_TYPES, default='Public')
#     verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.user.username


class OTP(models.Model):
    
    def Get_OTP():
        return random.randint(100000, 999999)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=Get_OTP)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username


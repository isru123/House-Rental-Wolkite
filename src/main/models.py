from django.db import models
import uuid

from users.models import Profile,Location

from .constants import CAR_BRANDS,TRANSMISSION_OPTIONS,MAXIMUM_AGE, MINMUM_AGE
from .utils import user_listing_path





class Listing(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    seller = models.ForeignKey(Profile, on_delete = models.CASCADE)
    brand = models.CharField(max_length=24, choices=CAR_BRANDS, default=None)
    model = models.CharField(max_length=64,)
    vin = models.CharField(max_length=17,)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24, default='white')
    description = models.TextField()
    engine = models.CharField(max_length=24,)
    transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path)
    
    
    def __str__(self):
        return f'{self.seller.user.username}\'s Listings - {self.model}'
    

class ListingSpaceOverview(models.Model):
    RADIO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    house_size = models.CharField(max_length=24)
    house_mate_no = models.CharField(max_length=24)
    bedroom_size = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Bedroom Size')
    bedroom_furnished = models.CharField(max_length=24)
    
    
    def __str__(self):
        return f'{self.house_size}'
    

class ListingHouseArea(models.Model):
    RADIO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    RADIO_CHOICES2 = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    RADIO_CHOICES3 = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    RADIO_CHOICES4 = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    RADIO_CHOICES5 = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    kitchen = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Kitchen')
    toilet = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Toilet')
    bathroom = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Bathroom')
    living_room = models.CharField(max_length=24, choices=RADIO_CHOICES4, verbose_name='Living Room')
    garden = models.CharField(max_length=24, choices=RADIO_CHOICES5, verbose_name='Garden')
    
    def __str__(self):
        return self.kitchen
    

class ListingHouseAmenities(models.Model):
    RADIO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    RADIO_CHOICES2 = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    RADIO_CHOICES3 = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    RADIO_CHOICES4 = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    bed = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Bed') 
    wifi = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Wifi')
    desk = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Desk')
    living_room_furnished = models.CharField(max_length=24, choices=RADIO_CHOICES4, verbose_name='Living Room Furnished')
    
    def __str__(self):
        return self.bed
    
    

class RentalConditions(models.Model):
    RADIO_CHOICES =[
        ('daily', 'Daily'),
        ('monthly', 'Monthly'),
        ('fortnight', 'Fortnight'),
    ]
    RADIO_CHOICES2 = [
        ('strict cancellation', 'Strict Cancellation'),
        ('flexible cancellation', 'Flexible Cancellation'),
    ]
    
    RADIO_CHOICES3 = [
        ('basic price', 'Basic Price'),
        ('advanced price', 'Advanced Price'),
    ]
    contract = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Contract Type')
    cancellation = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Cancellation Option')
    price = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Price')
    utility_costs = models.CharField(max_length=24)
    
    def __str__(self):
        return self.daily_contract
    

class RulesAndPreferences(models.Model):
    RADIO_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    RADIO_CHOICES2 = [
        ('any ', 'Any'),
        ('student ', 'Student'),
        ('working professional', 'Working Professional'),
    ]
    
    RADIO_CHOICES3 = [
        ('proof of identity', 'Proof of Identity'),
        ('proof of income', 'Proof of Income'),
        ('proof of occupation', 'Proof of Occupation'),
    ]
    
    
    gender = models.CharField(max_length=10, choices=RADIO_CHOICES, verbose_name='Gender')
    minimum_age = models.CharField(max_length=24, choices=MINMUM_AGE, default=None)
    maximum_age = models.CharField(max_length=24, choices=MAXIMUM_AGE, default=None)
    tenant = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Tenant Type')
    proof = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Proof for Tenant')
    

    
    def __str__(self):
        return self.gender
    
    
    
    
    

    
    
     
    
    
    
    def __str__(self):
        return f'{self.house_mate_no}\'s List space overview '
    
    
    
    
class ListArea(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # owner = models.ForeignKey(Profile, on_delete = models.CASCADE)
    kitchen = models.CharField(max_length=25)
    toilet  = models.CharField(max_length=25)
    bathroom = models.CharField(max_length=25)
    living_room = models.CharField(max_length=25)
    garden = models.CharField(max_length=25)
    
    
    def __str__(self):
        return f'{self.kitchen}\'s List area'
    

class ListAmenities(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # owner = models.ForeignKey(Profile, on_delete = models.CASCADE)
    bed= models.CharField(max_length=25)
    wifi = models.CharField(max_length=25)
    desk = models.CharField(max_length=25)
    living_room_furnished = models.CharField(max_length=25)
    
    
    def __str__(self):
        return f'{self.bed}\'s List amenities '
    
    
    

class ListRentalConditions(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # owner = models.ForeignKey(Profile, on_delete = models.CASCADE)
    daily_contract = models.CharField(max_length=25)
    fortnight_contract = models.CharField(max_length=25)
    monthly_contract = models.CharField(max_length=25)
    strict_cancellation = models.CharField(max_length=25)
    flexible_cancellation = models.CharField(max_length=25)
    basic_price = models.CharField(max_length=25)
    advanced_price = models.CharField(max_length=30)
    
    
    
    def __str__(self):
        return f'{self.daily_contract}\'s List rental conditions'
    




class ListRulesPreferences(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # owner = models.ForeignKey(Profile, on_delete = models.CASCADE)
    gender = models.CharField(max_length=25)
    min_age = models.CharField(max_length=25)
    max_age = models.CharField(max_length=25)
    any_tenant = models.CharField(max_length=25)
    student_tenant = models.CharField(max_length=25)
    working_pro_tenant = models.CharField(max_length=25)
    proof_of_identity = models.CharField(max_length=25)
    proof_of_occupation = models.CharField(max_length=25)
    proof_of_income = models.CharField(max_length=25)
    
    
    def __str__(self):
        return f'{self.gender}\'s List rules and preferences'
    
    


    
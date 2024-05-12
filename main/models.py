from django.db import models
import uuid
from django.utils import timezone
from users.models import Location,Profile
from django.utils.translation import gettext_lazy as _
from .constants import MAXIMUM_AGE, MINMUM_AGE,TRANSMISSION_OPTIONS,CAR_BRANDS
from .utils import user_listing_path
from django.core.validators import MaxValueValidator, MinValueValidator



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
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bed = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Bed') 
    wifi = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Wifi')
    desk = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Desk')
    living_room_furnished = models.CharField(max_length=24, choices=RADIO_CHOICES4, verbose_name='Living Room Furnished')
    
    def __str__(self):
           
            return f'ID {self.id} Listing House Amenities of {self.seller.user.username}'
 
    


class ListingSpaceOverview(models.Model):
   
    RADIO_CHOICES2 = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    house_size = models.CharField(max_length=24)
    house_mate_no = models.CharField(max_length=24)
    bedroom_size = models.CharField(max_length=24, verbose_name='Bedroom Size')
    bedroom_furnished = models.CharField(max_length=24, choices=RADIO_CHOICES2)
    
    
    def __str__(self):
           
            return f'ID {self.id} Listing Space Overview of {self.seller.user.username}'




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
    
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    kitchen = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Kitchen')
    toilet = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Toilet')
    bathroom = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Bathroom')
    living_room = models.CharField(max_length=24, choices=RADIO_CHOICES4, verbose_name='Living Room')
    garden = models.CharField(max_length=24, choices=RADIO_CHOICES5, verbose_name='Garden')
    
    def __str__(self):
           
            return f'ID {self.id} Listing House Area of {self.seller.user.username}' 
    

    

class RentalConditions(models.Model):
    
    RADIO_CHOICES =[
        ('shelter', 'Shelter'),
        ('business', 'Business'),
    ]
    RADIO_CHOICES2 = [
        ('strict cancellation', 'Strict Cancellation'),
        ('flexible cancellation', 'Flexible Cancellation'),
    ]
    
    RADIO_CHOICES3 = [
        ('basic price', 'Basic Price'),
        ('advanced price', 'Advanced Price'),
    ]
    
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    contract = models.CharField(max_length=24, choices=RADIO_CHOICES, verbose_name='Contract Type')
    cancellation = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Cancellation Option')
    price = models.CharField(max_length=24, choices=RADIO_CHOICES3, verbose_name='Price')
    utility_costs = models.CharField(max_length=24)
    
    def __str__(self):
           
            return f'ID {self.id} Listing Rental Conditions of {self.seller.user.username}'
    

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
   
    
    
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=RADIO_CHOICES, verbose_name='Gender')
    minimum_age = models.CharField(max_length=24, choices=MINMUM_AGE, default=None)
    maximum_age = models.CharField(max_length=24, choices=MAXIMUM_AGE, default=None)
    tenant = models.CharField(max_length=24, choices=RADIO_CHOICES2, verbose_name='Tenant Type')
    proof = models.CharField(max_length=24, verbose_name='Proof for Tenant')
    

    
    def __str__(self):
           
            return f'ID {self.id} Listing Rules and Preferences of {self.seller.user.username}'
    
    



class Image(models.Model):
       seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
       image1 = models.ImageField(upload_to=user_listing_path)
       image2 = models.ImageField(upload_to=user_listing_path)
       image3 = models.ImageField(upload_to=user_listing_path)
       image4 = models.ImageField(upload_to=user_listing_path)
       image5 = models.ImageField(upload_to=user_listing_path)
       description = models.CharField(max_length=255,
                                         verbose_name=_("Short description"))
       created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Created"))
       
       
       def __str__(self):
           
            return f'ID {self.id} Listing Images of {self.seller.user.username}'
    
    



    
    
class Listing(models.Model):
      RADIO_CHOICES = [
        ('private_room', 'Private Room'),
        ('shared_room', 'Shared Room'),
      ]
      id = models.UUIDField(primary_key = True, default = uuid.uuid4, unique=True, editable=False)
      created_at = models.DateTimeField(auto_now_add =True)
      updated_at = models.DateTimeField(auto_now =True)
      seller = models.ForeignKey(Profile, on_delete = models.CASCADE)
      location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
      house_kind = models.CharField(max_length=200,choices=RADIO_CHOICES, verbose_name='House Kind')
      description = models.TextField()
      price = models.PositiveSmallIntegerField()
      available_start = models.DateTimeField(default=timezone.now,null=True)
      available_end = models.DateTimeField(default=timezone.now,null=True)
      photo = models.ImageField(upload_to=user_listing_path)
      address = models.CharField(max_length=255)
      approved = models.BooleanField(default=False)
    #   rooms = models.ManyToManyField(Room)
      minimum_rental_period = models.CharField(max_length=200,choices=TRANSMISSION_OPTIONS)
      maximum_rental_period = models.CharField(max_length=200,choices=CAR_BRANDS)
      address = models.CharField(max_length=255)
      latitude = models.FloatField(blank=True, null=True)
      longitude = models.FloatField(blank=True, null=True)
      amenities = models.ManyToManyField(ListingHouseAmenities)
      listing_space_overview = models.ManyToManyField(ListingSpaceOverview)
      listing_house_area = models.ManyToManyField(ListingHouseArea)
      rental_condtion = models.ManyToManyField(RentalConditions)
      rules_and_preferences = models.ManyToManyField(RulesAndPreferences)
      image = models.ManyToManyField(Image)
      
    
      def __str__(self):
        sequential_id = Listing.objects.filter(created_at__lte=self.created_at).count()
        return f"ID {sequential_id} {self.seller.user.username}'s Listing"
    
    


class AddressOfListing(models.Model):
    Address = models.CharField(max_length=100)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.Address}'
    


    

    

# This model is used to store reviews made by users for properties
class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ])
    
    def __str__(self):
         return f'{self.reviewer.user.username}\' reviewd f{self.listing.seller.user.username}\'s Listing'
    
    
    

class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(default=None)
    
    
    def __str__(self):
        return f'{self.listing.title} listing liked by {self.profile.user.username}' 


    

class Upload(models.Model):
    TENANT_CHOICES = (
        ('Document', 'Document'),
        ('Photo', 'Photo')
    )
    tenant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    document = models.FileField(upload_to='uploads/documents/')
    photo = models.ImageField(upload_to='uploads/photos/')

    def __str__(self):
        return f"{self.document.name} - {self.photo.name}"
    
    
    
    
    
 
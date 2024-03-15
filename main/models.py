from django.db import models
import uuid

from users.models import Profile,Location

from .constants import MAXIMUM_AGE, MINMUM_AGE,TRANSMISSION_OPTIONS,CAR_BRANDS
from .utils import user_listing_path


    

# This model is used to store different types of amenities

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
        return self.contract
    

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
    

# This model is used to store information about rooms within properties
# class Room(models.Model):
#     name = models.CharField(max_length=200)
#     capacity = models.PositiveSmallIntegerField()


# class Image(models.Model):
#      image1 = models.ImageField(upload_to=user_listing_path)
#      image2 = models.ImageField(upload_to=user_listing_path)
#      image3 = models.ImageField(upload_to=user_listing_path)
#      image4 = models.ImageField(upload_to=user_listing_path)
#      image5 = models.ImageField(upload_to=user_listing_path)
#      alt_text = models.CharField(max_length=200)
    
    

# class Listing(models.Model):
#     id = models.UUIDField(primary_key = True, default = uuid.uuid4, unique=True, editable=False)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     seller = models.ForeignKey(Profile, on_delete = models.CASCADE)
#     brand = models.CharField(max_length=24, choices=CAR_BRANDS, default=None)
#     model = models.CharField(max_length=64,)
#     vin = models.CharField(max_length=17,)
#     mileage = models.IntegerField(default=0)
#     color = models.CharField(max_length=24, default='white')
#     description = models.TextField()
#     title = models.CharField(max_length=200)
#     engine = models.CharField(max_length=24,)
#     price = models.PositiveIntegerField()
#     transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTIONS, default=None)
#     location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
#     image = models.ImageField(upload_to=user_listing_path)
#     # rooms = models.ManyToManyField(Room)
#     amenities = models.ManyToManyField(ListingHouseAmenities, through='Amenity')
#     listing_space_overview = models.ManyToManyField(ListingSpaceOverview, through='ListingSpace')
#     listing_house_area = models.ManyToManyField(ListingHouseArea, through='HouseArea')
#     rental_condtion = models.ManyToManyField(RentalConditions, through='RentalCondition')
#     rules_and_preferences = models.ManyToManyField(RulesAndPreferences, through='Rules')
    
    
#     def __str__(self):
#         return f'{self.seller.user.username}\'s Listings - {self.model}'
    
class Listing(models.Model):
      id = models.UUIDField(primary_key = True, default = uuid.uuid4, unique=True, editable=False)
      created_at = models.DateTimeField(auto_now_add =True)
      updated_at = models.DateTimeField(auto_now =True)
      seller = models.ForeignKey(Profile, on_delete = models.CASCADE)
      location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
      title = models.CharField(max_length=200)
      description = models.TextField()
      price = models.PositiveSmallIntegerField()
      available_start = models.DateTimeField(null=True)
      available_end = models.DateTimeField(null=True)
      # photos = models.ManyToManyField('Image')
    #   rooms = models.ManyToManyField(Room)
      amenities = models.ManyToManyField(ListingHouseAmenities, through='Amenity')
      listing_space_overview = models.ManyToManyField(ListingSpaceOverview, through='ListingSpace')
      listing_house_area = models.ManyToManyField(ListingHouseArea, through='HouseArea')
      rental_condtion = models.ManyToManyField(RentalConditions, through='RentalCondition')
      rules_and_preferences = models.ManyToManyField(RulesAndPreferences, through='Rules')
    
    
      def __str__(self):
          return f'{self.seller.user.username}\'s Listings'
    
    
    


    
# This model is used to store booking information made by guests
class Booking(models.Model):
    guest = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(default=None)
    check_out_date = models.DateTimeField(default=None)
    # rooms = models.ManyToManyField(Room)
    
    
    
    def __str__(self):
         return f'{self.listing.title}\' listing booked'
    
    
    
    

# # This model is used to store details of room bookings within a general booking
# class RoomBooking(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
#     booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
#     adults = models.PositiveSmallIntegerField()
#     children = models.PositiveSmallIntegerField()
    
    
   
#     def __str__(self):
#          return f'{self.listing.title}\'  booked'
    
    
    

# This model is used to store reviews made by users for properties
class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    
    def __str__(self):
         return f'{self.listing.title}\' listing reviewd'
    
    
    

class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(default=None)
    
    
    def __str__(self):
        return f'{self.listing.title} listing liked by {self.profile.user.username}' 

    
    


# This model is used to link amenities to properties
class Amenity(models.Model):
     Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='property_amenities')
     amenity_type = models.ForeignKey(ListingHouseAmenities, on_delete=models.CASCADE, default=None, related_name='amenity_type')


class ListingSpace(models.Model):
     Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_spaces')
     space_overview = models.ForeignKey(ListingSpaceOverview, on_delete=models.CASCADE, default=None, related_name='space_overview')
    
class HouseArea(models.Model):
     Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='Listing_house_area')
     house_area = models.ForeignKey(ListingHouseArea, on_delete=models.CASCADE, default=None, related_name='house_area')
    
class RentalCondition(models.Model):
     Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='rental_conditions')
     rental_conditions = models.ForeignKey(RentalConditions, on_delete=models.CASCADE,default=None, related_name='rental_conditions')

class Rules(models.Model):
     Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='Listing_rules')
     rules_and = models.ForeignKey(RulesAndPreferences, on_delete=models.CASCADE, default=None, related_name='rules_and_preferences')
    
      
    
    
    
    
 
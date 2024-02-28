from django.db import models
import uuid

from users.models import Profile,Location
from .constants import CAR_BRANDS,TRANSMISSION_OPTIONS
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
    image = models.ImageField()
    
    
    def __str__(self):
        return f'{self.seller.user.username}\'s Listings - {self.model}'
    

class ListingSpaceOverview(models.Model):
    house_size = models.CharField(max_length=24)
    house_mate_no = models.CharField(max_length=24)
    bedroom_size = models.CharField(max_length=24)
    bedroom_furnished = models.CharField(max_length=24)
    
    
    def __str__(self):
        return f'{self.house_size}'
    

    
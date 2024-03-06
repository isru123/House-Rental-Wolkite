from  django import forms  

from .models import Listing,ListingSpaceOverview,ListingHouseArea,ListingHouseAmenities,RentalConditions, RulesAndPreferences

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = {'title', 'price', 'description'}
        
        

class ListingSpaceOverviewForm(forms.ModelForm):
    
    class Meta:
        model = ListingSpaceOverview
        fields = '__all__'

class ListingHouseAreaForm(forms.ModelForm):
    
     class Meta:
        model = ListingHouseArea
        fields = '__all__'
    
    
class ListingHouseAmenitiesForm(forms.ModelForm):
    
     class Meta:
        model = ListingHouseAmenities
        fields = {'bed','wifi','desk','living_room_furnished'} 
    

class RentalConditionsForm(forms.ModelForm):
    
     class Meta:
        model = RentalConditions
        fields = '__all__'


class RulesAndPreferencesForm(forms.ModelForm):
    
     class Meta:
         model = RulesAndPreferences
         fields = '__all__'
    

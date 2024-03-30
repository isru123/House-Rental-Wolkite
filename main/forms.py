from  django import forms  
from django.utils.translation import  gettext_lazy as _
from .models import Booking,Review,Listing,ListingSpaceOverview,ListingHouseArea,ListingHouseAmenities,RentalConditions, RulesAndPreferences



class ListingForm(forms.ModelForm):
    available_start = forms.DateField(label=_("Available Start"), widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'id_available_start'}))
    available_end = forms.DateField(label=_("Available End"), widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'id_available_end'}))
    image = forms.ImageField(label=_("Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class': 'image-input', 'id': 'id_image'}))
    # house_kind = forms.ChoiceField(label=_("House Kind"), choices=AVAILABLE_HOUSE_KINDS, widget=forms.Select(attrs={'class': 'bold-input','placeholder': 'House Type'}))
    address = forms.CharField(label=_("Address"), widget=forms.TextInput)
    price = forms.DecimalField(label=_("Price"), widget=forms.TextInput(attrs={'class': 'bold-input'}))
    # minimum_rental_period = forms.ChoiceField(label=_("Minimum Rental Period"), choices=AVAILABLE_HOUSE_KINDS, widget=forms.Select(attrs={'class': 'bold-input','placeholder': 'Minimum Rental Perio'}))
    # maximum_rental_period = forms.ChoiceField(label=_("Maximum Rental Period"), choices=AVAILABLE_HOUSE_KINDS, widget=forms.Select(attrs={'class': 'bold-input','placeholder': 'Maximum Rental Period'}))
        
    class Meta:
        model = Listing
        fields = ['house_kind', 'address', 'price', 'available_start', 'available_end', 'minimum_rental_period','maximum_rental_period','image']
        labels = {
            'house_kind': _('House Kind'),
            'address': _('Address'),
            'price': _('Price'),
        }
        
        
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
    

 
 
class ReviewForm(forms.ModelForm):
     class Meta:
         model =  Review
         fields = '__all__'


class BookingForm(forms.ModelForm):
     class Meta:
         model = Booking
         fields = '__all__'
         
         
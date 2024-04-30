from  django import forms  
from django.utils.translation import  gettext_lazy as _
from .models import Image,Listing,ListingSpaceOverview,ListingHouseArea,ListingHouseAmenities,RentalConditions, RulesAndPreferences



class ListingForm(forms.ModelForm):
    available_start = forms.DateField(label=_("Available Start"), widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'id_available_start'}))
    available_end = forms.DateField(label=_("Available End"), widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'id_available_end'}))
    # image = forms.ImageField(label=_("Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class': 'image-input', 'id': 'id_image'}))
    # house_kind = forms.ChoiceField(label=_("House Kind"), choices=AVAILABLE_HOUSE_KINDS, widget=forms.Select(attrs={'class': 'bold-input','placeholder': 'House Type'}))
    address = forms.CharField(label=_("Address"), widget=forms.TextInput)
    price = forms.DecimalField(label=_("Price"), widget=forms.TextInput(attrs={'class': 'bold-input'}))
    # minimum_rental_period = forms.ChoiceField(label=_("Minimum Rental Period"), choices=AVAILABLE_HOUSE_KINDS, widget=forms.Select(attrs={'class': 'bold-input','placeholder': 'Minimum Rental Perio'}))
    # maximum_rental_period = forms.ChoiceField(label=_("Maximum Rental Period"), choices=AVAILABLE_HOUSE_KINDS, widget=forms.Select(attrs={'class': 'bold-input','placeholder': 'Maximum Rental Period'}))
        
    class Meta:
        model = Listing
        fields = ['house_kind', 'address', 'price', 'available_start', 'available_end', 'minimum_rental_period','maximum_rental_period']
        labels = {
            'house_kind': _('House Kind'),
            'address': _('Address'),
            'price': _('Price'),
        }
        
        
class ListingSpaceOverviewForm(forms.ModelForm):
    
    class Meta:
        model = ListingSpaceOverview
        fields = '__all__'
        exclude = ['seller']

class ListingHouseAreaForm(forms.ModelForm):
    
     class Meta:
        model = ListingHouseArea
        fields = '__all__'
        exclude = ['seller']
    
    
class ListingHouseAmenitiesForm(forms.ModelForm):
    
     class Meta:
        model = ListingHouseAmenities
        fields = {'bed','wifi','desk','living_room_furnished'} 
    

class RentalConditionsForm(forms.ModelForm):
    
     class Meta:
        model = RentalConditions
        fields = '__all__'
        exclude = ['seller']


class RulesAndPreferencesForm(forms.ModelForm):
    
     class Meta:
         model = RulesAndPreferences
         fields = '__all__'
         exclude = ['seller']
    

 
 

class ImageForm(forms.ModelForm):
    description = forms.CharField(label=_("Description"), widget=forms.Textarea)
    image1 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'style': 'width: 300px; height: 100px;'}))
    image2 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'style': 'width: 300px; height: 50px;'}))
    image3 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'style': 'width: 300px; height: 50px;'}))
    image4 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'style': 'width: 300px; height: 100px;'}))
    image5 = forms.ImageField(widget=forms.ClearableFileInput(attrs={'style': 'width: 300px; height: 50px;'}))
    class Meta:
        model = Image
        fields = {'image1','image2','image3','image4','image5','description'}
        exclude = ['seller'] 


class RentalFilterForm(forms.Form):
    move_in_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Move-in Date'
    )
    move_out_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Move-out Date'
    )
        
         
from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['document', 'photo']

         
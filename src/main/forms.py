from  django import forms  

from .models import Listing,ListingSpaceOverview

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage', 'color', 'description', 
                  'engine', 'transmission', 'image'}
        
        

class ListingSpaceOverviewForm(forms.ModelForm):
    model = ListingSpaceOverview
    fields = {'house_size','house_mate_no','bedroom_size','bedroom_furnished'}
    
    
    
    
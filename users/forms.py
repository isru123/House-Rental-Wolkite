from django import forms
from .models import Location,Profile
from localflavor.us.forms import USZipCodeField

from django.contrib.auth.models import User
from .widgets import CustomPictureImageFieldWidget

class UserForm(forms.ModelForm):
     username = forms.CharField(disabled=False)
    
     class Meta:
         model = User
         fields = {'username', 'first_name', 'last_name'}
        

class ProfileForm(forms.ModelForm):
     photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
     bio = forms.Textarea()
    
     class Meta:
         model = Profile
         fields = {'photo', 'bio','address','contact_No','userType'}
        
    

class LocationForm(forms.ModelForm):
    
    address_1 = forms.CharField(required=True)
    address_2 = forms.CharField(required=True)
    
    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city'}
    
    

        
        
        
from  django import forms  

from users.models import Profile
from users.widgets import CustomPictureImageFieldWidget

class AdminProfileForm(forms.ModelForm):
    
     photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
     bio = forms.Textarea()
    
     class Meta:
         model = Profile
         fields = {'photo', 'bio','address','contact_No','userType'}
        
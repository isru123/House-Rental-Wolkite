from  django import forms  
from django.utils.translation import  gettext_lazy as _
<<<<<<< HEAD
from .models import Image,Listing,ListingSpaceOverview,ListingHouseArea,ListingHouseAmenities,RentalConditions, RulesAndPreferences

=======
from .models import Image,Review,Listing,Document,ListingSpaceOverview,ListingHouseArea,ListingHouseAmenities,RentalConditions, RulesAndPreferences,AddressOfListing,Upload
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9


class ListingForm(forms.ModelForm):
    available_start = forms.DateField(label=_("Available Start"), widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker', 'id': 'id_available_start'}))
   
 
    price = forms.DecimalField(label=_("Price"), widget=forms.TextInput(attrs={'class': 'bold-input'}))
  
    class Meta:
        model = Listing
        fields = ['house_kind', 'price', 'available_start','id_photo','house_map']
        labels = {
            'house_kind': _('House Kind'),
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
        exclude = ['seller','contract','cancellation','price','utility_costs']


class RulesAndPreferencesForm(forms.ModelForm):
    
    
    
    class Meta:
         model = RulesAndPreferences
         fields = '__all__'
         exclude = ['seller']
    

 
 

class ImageForm(forms.ModelForm):
    description = forms.CharField(label=_("Description"), widget=forms.Textarea(attrs={'style':'width: 300px; height: 100px;'}))
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
<<<<<<< HEAD


# class ReviewForm(forms.ModelForm):
#     review_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Your Review'}))
#     rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 6)])
=======
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9
    
    class Meta:
        model = Listing
        fields = ['move_in_date', 'move_out_date']

<<<<<<< HEAD
         
=======
class ReviewForm(forms.ModelForm):
    RATING_CHOICES = (
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    )

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'rating-input', 'style': 'display: inline-block;'})
    )
    review_text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Your Review'})
    )
    hidden_rating = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Review
        fields = ['rating', 'review_text']

        
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit Review'))
         

class AddressForm(forms.Form):
    address = forms.ModelChoiceField(
        queryset=AddressOfListing.objects.all(),
        widget=autocomplete.ModelSelect2(url='address-autocomplete')
    )
    
    class Meta:
        model = AddressOfListing
        fields = ['Address']
        

class DocumentForm(forms.ModelForm):
    id_photo = forms.ImageField()
    house_map = forms.ImageField()
    class Meta:
        model = Document
        fields = ('id_photo', 'house_map')
        


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['photo','id_proof','income_proof','profession_proof']
        

    
        
    
        
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

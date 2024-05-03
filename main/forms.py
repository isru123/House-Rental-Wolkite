from  django import forms  
from django.utils.translation import  gettext_lazy as _
from .models import Image,Review,Listing,Document,ListingSpaceOverview,ListingHouseArea,ListingHouseAmenities,RentalConditions, RulesAndPreferences,AddressOfListing
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from dal import autocomplete


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
        fields = ['house_kind', 'price','address', 'available_start', 'available_end']
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
        exclude = ['seller']


class RulesAndPreferencesForm(forms.ModelForm):
    
    RADIO_CHOICES3 = [
    ('proof of identity', 'Proof of Identity'),
    ('proof of income', 'Proof of Income'),
    ('proof of occupation', 'Proof of Occupation'),
         ]
    
    Document = forms.MultipleChoiceField(
        choices=RADIO_CHOICES3,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    
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
        widget=forms.RadioSelect(attrs={'class': 'rating-input'})
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
         

# class AddressForm(forms.Form):
#     address = forms.ModelChoiceField(
#         queryset=AddressOfListing.objects.all(),
#         widget=autocomplete.ModelSelect2(url='address-autocomplete')
#     )
    
#     class Meta:
#         model = AddressOfListing
#         fields = ['Address']
        

class DocumentForm(forms.ModelForm):
    id_photo = forms.ImageField()
    house_map = forms.ImageField()
    class Meta:
        model = Document
        fields = ('id_photo', 'house_map')
        
        
    
        
    
        
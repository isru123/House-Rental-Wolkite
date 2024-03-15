from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing,LikedListing
from .forms import ListingForm
from users.forms import LocationForm
from django.core.files.storage import DefaultStorage
from importlib import reload
from formtools.wizard.views import SessionWizardView
from .filters import ListingFilter

from .models import (
    Listing,
    ListingSpaceOverview,
    ListingHouseArea,
    ListingHouseAmenities,
    RentalConditions,
    RulesAndPreferences,
)

from .forms import (
    ListingForm,
    ListingSpaceOverviewForm,
    ListingHouseAreaForm,
    ListingHouseAmenitiesForm,
    RentalConditionsForm,
    RulesAndPreferencesForm,
)


def main_view(request):
    return render(request, 'main/homepage/home.html', {'name': 'home'})



def master_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    
    if hasattr(request.user, 'profile'):
        
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    
        liked_listings_ids = [l[0] for l in user_liked_listings ]
    else:
        liked_listings_ids = []
    
    return render(request, 'main/major/master.html',  {'listing_filter': listing_filter,
                                               'liked_listings_ids': liked_listings_ids})

   

def detail_list_view(request):
    return render(request, 'components/detail_list_view.html')

 
def owner_view(request):
    return render(request, 'main/owner/first.html')


def dashboard_view(request):
    return render(request, 'main/owner/dashboard.html')

def listing_view(request):
    return render(request, 'main/owner/listing.html')

def owner_second_view(request):
    return render(request, 'main/owner/second.html')


class multistepformsubmission(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = 'main/owner/listing.html'
    form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm,RentalConditionsForm,RulesAndPreferencesForm]
    
    
    def done(self, form_list, **kwargs):
         # Retrieve form data from the form_list
        form_data = [form.cleaned_data for form in form_list]
        
        # Extract seller_id from the form data
        # seller_id = form_data[0]['seller']

        # Create instances of the model objects
        listing = Listing.objects.create(**form_data[0])
        space_overview = ListingSpaceOverview.objects.create(**form_data[1])
        house_area = ListingHouseArea.objects.create(**form_data[2])
        house_amenities = ListingHouseAmenities.objects.create(**form_data[3])
        rental_conditions = RentalConditions.objects.create(**form_data[4])
        rules_preferences = RulesAndPreferences.objects.create(**form_data[5])

        # Save the model instances to the database
        listing.save()
        space_overview.save()
        house_area.save()
        house_amenities.save()
        rental_conditions.save()
        rules_preferences.save()
        return HttpResponse('form submitted!')
    
    
def single_house_view(request):
    return render(request, 'components/single_house_view.html')



def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    
    liked_listing, created  = LikedListing.objects.get_or_create(profile=request.user.profile, listing=listing)
    
    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
    
    return JsonResponse(
        {
            'is_liked_by_user': created,
        }
    )





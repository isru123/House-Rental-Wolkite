from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing,LikedListing
from .forms import ListingForm
from .forms import ListingSpaceOverviewForm,ListingHouseAreaForm,ListingHouseAmenitiesForm,RentalConditionsForm, RulesAndPreferencesForm
from django.core.files.storage import DefaultStorage
from importlib import reload
from formtools.wizard.views import SessionWizardView
from .filters import ListingFilter

def main_view(request):
    return render(request, 'main/homepage/home.html', {'name': 'home'})



@login_required
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





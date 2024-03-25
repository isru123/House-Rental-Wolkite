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


# Now you can use 'formatted_datetime' for serialization or JSON conversion

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

# def listing_view(request):
#     return render(request, 'main/owner/listing.html')

def owner_second_view(request):
    return render(request, 'main/owner/second.html')


# def ListingView(request):
    
#     if request.method == 'POST':
        
#         listing_form = ListingForm(request.POST)
        
#         if listing_form.is_valid():
            
#             request.session['listing_data'] = listing_form.cleaned_data
            
#             return redirect('listing_space_overview')
        
#         else:
            
#             listing_form = ListingForm()
            
#     else:
        
#         listing_form = ListingForm()
             
#         return render(request, 'main/owner/listing.html', {'listing_form': listing_form})
    
#     # # Serialize the data, handling datetime objects
#     # serialized_data = serialize('json', data, default=handle_datetime)

#     # # Return the serialized data as an HTTP response
#     # return HttpResponse(serialized_data, content_type='application/json')
    
    

# def SpaceOverview(request):
#     if request.method == 'POST':
#         listing_space_form = ListingSpaceOverviewForm(request.POST)
        
#         if listing_space_form.is_valid():
            
#             request.session['space_overview_data'] = listing_space_form.cleaned_data
            
#             return redirect('listing_house_area')
        
#         else:
            
#             listing_space_form = ListingSpaceOverviewForm()
            
#     else:
        
#         listing_space_form = ListingSpaceOverviewForm()
            
#         return render(request, 'space_overview.html', {'form': listing_space_form})
    
    
# def ListingHouseView(request):
#     if request.method == 'POST':
#         form = ListingHouseAreaForm(request.POST)
        
#         if form.is_valid():
            
#             request.session['listing_house_data'] = form.cleaned_data
            
#             return redirect('listing_house_amenities')
        
#         else:
            
#             form = ListingHouseAreaForm()
            
#         return render(request, 'listing_house.html', {'form': form})
    
# def ListingAmenitiesView(request):
    
#     if request.method == 'POST':
#         form = ListingHouseAmenitiesForm(request.POST)
        
#         if form.is_valid():
            
#             request.session['listing_amenities_data'] = form.cleaned_data
            
#         return redirect('listing_rental_condition')
    
#     else:
        
#         form = ListingHouseAmenitiesForm()
        
#     return render(request, 'listing_amenities.html', {'form': form})

# def ListingRentalConditionView(request):
    
#     if request.method == 'POST':
        
#         form = RentalConditionsForm(request.POST)
        
#         if form.is_valid():
            
#             request.session['listing_rental_condition_data'] = form.cleaned_data
            
#         return redirect('listing_preferences')
    
#     else:
        
#         form = RentalConditionsForm()
    
#     return render(request, 'listing_rental_condition.html', {'form': form})


# def ListingRulesView(request):
    
#     if request.method == 'POST':
        
#         form = RulesAndPreferencesForm(request.POST)
        
#         if form.is_valid():
            
#             request.session['listing_preferences_data'] = form.changed_data
        
#         return redirect('listing_images')
    
#     else:
        
#         form = RulesAndPreferencesForm()
        
#     return render(request, 'listing_preferences.html', {'form': form})



   





@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing_location = listing_location
                listing.save()
                messages.info(request, f'{listing.title} Listing Posted Successfully!')
                return redirect('master')
        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.'
            )
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
        
        return render(request, 'main/owner/listing.html', {'listing_form': listing_form, 'location_form': location_form})
    


 
@login_required  
def single_house_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'components/single_house_view.html',{'listing': listing})
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing')
        return redirect('home')
    
      
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















# class multistepformsubmission(SessionWizardView):
#     file_storage = DefaultStorage()
#     template_name = 'main/owner/listing.html'
#     form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm,RentalConditionsForm,RulesAndPreferencesForm]
    
    
#     def done(self, form_list, **kwargs):
#          # Retrieve form data from the form_list
#         form_data = [form.cleaned_data for form in form_list]
        
#         # # Extract seller_id from the form data
#         # # seller_id = form_data[0]['seller']
#         # listing = ListingForm.cleaned_data.get()
#         # # Create instances of the model objects
#         # listing = Listing.objects.create(**form_data[0])
#         # space_overview = ListingSpaceOverview.objects.create(**form_data[1])
#         # house_area = ListingHouseArea.objects.create(**form_data[2])
#         # house_amenities = ListingHouseAmenities.objects.create(**form_data[3])
#         # rental_conditions = RentalConditions.objects.create(**form_data[4])
#         # rules_preferences = RulesAndPreferences.objects.create(**form_data[5])

#         # # Save the model instances to the database
#         # listing.save()
#         # space_overview.save()
#         # house_area.save()
#         # house_amenities.save()
#         # rental_conditions.save()
#         # rules_preferences.save()
        
#         listing_instance = form_list[0].save()  # Assuming ListingForm is the first form
#         space_overview_instance = form_list[1].save(commit=False)
#         space_overview_instance.listing = listing_instance
#         space_overview_instance.save()
        
#         return HttpResponse('form submitted!')
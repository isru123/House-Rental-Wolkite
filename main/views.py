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
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    
    if hasattr(request.user, 'profile'):
        
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    
        liked_listings_ids = [l[0] for l in user_liked_listings ]
    else:
        liked_listings_ids = []
    
    return render(request, 'main/homepage/home.html',  {'listing_filter': listing_filter,
                                               'liked_listings_ids': liked_listings_ids})



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



   





# @login_required(login_url='/login/')
# def list_view(request):
#     if request.method == 'POST':
#         try:
#             listing_form = ListingForm(request.POST, request.FILES)
#             location_form = LocationForm(request.POST, )
#             if listing_form.is_valid() and location_form.is_valid():
#                 listing = listing_form.save(commit=False)
#                 listing_location = location_form.save(commit=False)
#                 listing_location = location_form.save()
#                 listing.seller = request.user.profile
#                 listing_location = listing_location
#                 listing.save()
               
#                 return redirect('listing_space_overview')
#                 # messages.info(request, f'{listing.title} Listing Posted Successfully!')
#                 # return redirect('master')
            
#             else:
#                 listing_form = ListingForm()
#                 location_form = LocationForm()
                
#         except Exception as e:
#             print(e)
#             messages.error(
#                 request, 'An error occured while posting the listing.'
#             )
#     elif request.method == 'GET':
#         listing_form = ListingForm()
#         location_form = LocationForm()
        
#         return render(request, 'main/owner/listing.html', {'listing_form': listing_form, 'location_form': location_form})
    





# def SpaceOverview(request):
#       if request.method == 'POST':
#           listing_space_form = ListingSpaceOverviewForm(request.POST,request.FILES)
        
#           if listing_space_form.is_valid():
#               listing_space_overview = listing_space_form.save(commit=False)
#               listing_space_overview.seller = request.user.profile
#               listing_space_overview.save()
#             #   request.session['space_overview_data'] = listing_space_form.cleaned_data
            
#               return redirect('listing_house_area')
        
#           else:
            
#               listing_space_form = ListingSpaceOverviewForm()
            
#       else:
        
#           listing_space_form = ListingSpaceOverviewForm()
            
#           return render(request, 'main/owner/space_overview.html', {'listing_space_form': listing_space_form})
    
    
    
    
    

 
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






class multistepformsubmission(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = 'main/owner/multistep.html'
    form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm,RentalConditionsForm,RulesAndPreferencesForm]
    
    
    def done(self, form_list, **kwargs):
     
        form_data = [form.cleaned_data for form in form_list]
        seller = self.request.user.profile 
        listing = Listing(title = form_data[0]['title'], description = form_data[0]['description'],
                          price = form_data[0]['price'], available_start = form_data[0]['available_start'],
                          available_end = form_data[0]['available_end'] , image = form_data[0]['image'],
                          seller=seller )
        listing.save()
        
        listing_space = ListingSpaceOverview(house_size = form_data[1]['house_size'],
                                             house_mate_no = form_data[1]['house_mate_no'],
                                            bedroom_size = form_data[1]['bedroom_size'] ,
                                            bedroom_furnished = form_data[1]['bedroom_furnished'])
        
        listing_space.save()
        
        listing_house = ListingHouseArea(kitchen = form_data[2]['kitchen'],
                                        toilet = form_data[2]['toilet'],
                                        bathroom = form_data[2]['bathroom'],
                                        living_room = form_data[2]['living_room'],
                                        garden = form_data[2]['garden'])
        
        listing_house.save()
        
        
        listing_amenities = ListingHouseAmenities(
            bed = form_data[3]['bed'],
            wifi = form_data[3]['wifi'],
            desk = form_data[3]['desk'],
            living_room_furnished = form_data[3]['living_room_furnished']
        )
        
        listing_amenities.save()
        
        
        rental_condition = RentalConditions(
            contract = form_data[4]['contract'],
            cancellation = form_data[4]['cancellation'],
            price = form_data[4]['price'],
            utility_costs = form_data[4]['utility_costs']
        )
        
        rental_condition.save()
        
        
        rules_preferences = RulesAndPreferences(
            gender =  form_data[5]['gender'],
            minimum_age = form_data[5]['minimum_age'],
            maximum_age = form_data[5]['maximum_age'],
            tenant = form_data[5]['tenant'],
            proof = form_data[5]['proof']
        )
        
        rules_preferences.save()
        
        
        data = Listing.objects.all()
        
        
        return render(self.request, 'main/owner/done.html', {'data': data})
    
    
def payement(request):
    return render(request, 'includes/payemnts.html')


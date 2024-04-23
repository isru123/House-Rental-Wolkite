from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing,LikedListing
from .forms import ListingForm,RentalFilterForm
from users.forms import LocationForm
from django.core.files.storage import DefaultStorage
from importlib import reload
from formtools.wizard.views import SessionWizardView
from .filters import ListingFilter
from users.forms import UserForm,ProfileForm,LocationForm
from opencage.geocoder import OpenCageGeocode
from django.conf import settings
from django.db.models import Q
from decimal import Decimal
from django.utils.html import format_html
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
import uuid
from datetime import datetime
from message.models import ConversationMessage
import requests
import folium
import pandas as pd
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Now you can use 'formatted_datetime' for serialization or JSON conversion

from .models import (
    Listing,
    ListingSpaceOverview,
    ListingHouseArea,
    ListingHouseAmenities,
    RentalConditions,
    RulesAndPreferences,
    Image,
    Review,
)

from .forms import (
    ListingForm,
    ListingSpaceOverviewForm,
    ListingHouseAreaForm,
    ListingHouseAmenitiesForm,
    RentalConditionsForm,
    RulesAndPreferencesForm,
    ImageForm,
    ReviewForm,
)


def main_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    
    # if hasattr(request.user, 'profile'):
        
    #     user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    
    #     liked_listings_ids = [l[0] for l in user_liked_listings ]
    # else:
    #     liked_listings_ids = []
    
    return render(request, 'main/homepage/home.html',  {'listing_filter': listing_filter,
                                            #    'liked_listings_ids': liked_listings_ids
                                            })



def master_view(request):
    all_listings  = Listing.objects.all()
    listing_filter  = ListingFilter(request.GET, queryset=all_listings )
   
    # listings = listings.prefetch_related('rules_and_preferences')
    
    
    # if hasattr(request.user, 'profile'):
        
    #     # user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing')
    
    #     liked_listings_ids = [l[0] for l in user_liked_listings ]
    # else:
    #     liked_listings_ids = []
        
        
     # Fetch related data using prefetch_related
    filtered_listings = listing_filter.qs.prefetch_related(
        'rules_and_preferences',
        'amenities',
        'listing_space_overview',
        'listing_house_area',
        'rental_condition',
        'image'
    )
    return render(request, 'main/major/master.html',  {'listing_filter': listing_filter,
                                               'filtered_listings': filtered_listings})
    #     liked_listings_ids = [l[0] for l in user_liked_listings ]
    # else:
    #     liked_listings_ids = []
    
    # return render(request, 'main/major/master.html',  {'listing_filter': listing_filter
    #                                         #    'liked_listings_ids': liked_listings_ids
    #                                         })

   

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







def map_view(request):
    listings = Listing.objects.all()
    geocoder = OpenCageGeocode(settings.OPENCAGE_API_KEY)

    for listing in listings:
        if not listing.latitude or not listing.longitude:
            results = geocoder.geocode(listing.address)
            if results and len(results):
                first_result = results[0]
                listing.latitude = first_result['geometry']['lat']
                listing.longitude = first_result['geometry']['lng']
                listing.save()

    context = {
        'listings': listings,
        'opencage_api_key': settings.OPENCAGE_API_KEY,
    }
    
    return render(request, 'main/major/location.html', context)












# def map_view(request):
#     if request.method == 'POST':
#     # listing_id = request.GET.get('listing_id')

#     # # Load the CSV data containing location information
#     # data = pd.read_csv('data/location.csv',encoding='utf-8')
#         address = request.POST.get('address')
#         response = requests.get(
#             f'settings.OPENCAGE_API_KEY
#         )
#         data = response.json()
#         # Check if the response contains the 'status' key
#         if 'status' in data and data['status'] == 'OK':
#         # Extract latitude and longitude from the response
#         # if data['status'] == 'OK':
#             latitude = data['results'][0]['geometry']['location']['lat']
#             longitude = data['results'][0]['geometry']['location']['lng']

#             # Create a map object
#             map = folium.Map(location=[latitude, longitude], zoom_start=12)

#             # Add a marker for the listing's location
#             marker = folium.Marker(location=[latitude, longitude], popup='Selected Location')
#             marker.add_to(map)

#             # Pass the map object to the template
#             context = {'map': map._repr_html_()}
#             return render(request, 'main/major/location.html', context)

#     return render(request, 'main/major/location.html')
    
    
    # Create a map with an initial view
    # map = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=10)

    # # Iterate through the data to add markers for each location
    # for _, row in data.iterrows():
    #     location = [row['Latitude'], row['Longitude']]
    #     name = row['Location Name']
        
        
    #     # Create a marker for each location
    #     marker = folium.Marker(location=location, popup=name)
    #     marker.add_to(map)

    # # Add a marker for the selected listing's location
    # if listing_id:
    #     listing = Listing.objects.get(id=listing_id)
    #     selected_location = [listing.latitude, listing.longitude]
    #     marker = folium.Marker(location=selected_location, popup='Selected Location')
    #     marker.add_to(map)

    #     # Pan to the selected location
    #     map.pan_to(selected_location)

    # # Pass the map object to the template
    # context = {'map': map._repr_html_()}
    # return render(request, 'main/major/location.html', context)






# def get_coordinates(address):
#     url = 'https://map-geocoding.p.rapidapi.com/json'
#     params = {
#         'address': address,
#         'key': '41bf648085msh064da0a40c524c0p18fb1cjsn79660b9868ab'  # Replace with your actual API key
#     }
#     response = requests.get(url, params=params)
#     data = response.json()

#     if data['status'] == 'OK':
#         result = data['results'][0]
#         latitude = result['geometry']['location']['lat']
#         longitude = result['geometry']['location']['lng']
#         return latitude, longitude

#     return None, None
    
    




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
    
    
    
    
    

 
# @login_required  
# def single_house_view(request, id):
#     # try:
#     #     listing = Listing.objects.get(id=id)
#     #     if listing is None:
#     #         raise Exception
#      #   return render(request, 'payment/single_house_view.html')
#     # except Exception as e:
#     #     messages.error(request, f'Invalid UID {id} was provided for listing')
#     #     return redirect('home')
#      product = Listing.objects.get(id=id)
#      context = {
#         'product': product
#      }
#      return render(request, 'components/single_house_view.html', context)


def single_house_view(request, id):
    filtered_listings = None 
    if request.method == 'POST':
        form = RentalFilterForm(request.POST)
        if form.is_valid():
            move_in_date = form.cleaned_data['move_in_date']
            move_out_date = form.cleaned_data['move_out_date']
            filtered_listings = Listing.objects.filter(
                Q(available_start=move_in_date, available_end=move_in_date) |
                Q(available_start=move_out_date, available_end=move_out_date)
            )
            # Render the filtered listings in the template
    else:
        form = RentalFilterForm()
    # return render(request, 'components/rental_search.html', {'form': form , 'filtered_listings':filtered_listings})
   
    try:
        listing = get_object_or_404(Listing, id=id)
        reviews = listing.reviews.all()
        review_form = ReviewForm(request.POST)
        # listing = Listing.objects.get(id=id)
        conversation_id = uuid.uuid4()  # Generate a UUID
        latitude = request.GET.get('lat')
        longitude = request.GET.get('lng')
        if listing is None:
             raise Exception
         
        # review_form = ReviewForm()  # Create a new instance of the review form
        
        
        # form = ReviewForm(request.GET)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.listing = listing
            review.reviewer = request.user.profile
            review.save()
            messages.success(request, 'Review added successfully.')
            return redirect('single_house_view', id=id)

        # reviews = Review.objects.filter(listing=listing)
        
        return render(request, 'components/single_house_view.html', {"listing": listing, 'form': form ,
                                        'filtered_listings':filtered_listings, 'conversation_id':conversation_id,'reviews':reviews,'review_form': review_form,'latitude': latitude,'longitude': longitude})
    except Listing.DoesNotExist:
        messages.error(request, f'Invalid UID {id} was provided for listing')
        # return redirect('home')
        return redirect('new', product_id=listing.id, conversation_id=conversation_id)


# def single_house_view(request, id):
#     try:
#         product = Listing.objects.get(id=id)
#         conversation_id = uuid.uuid4()  # Generate a UUID

#         # Check if the current user is the seller
#         user_is_seller = request.user.is_authenticated and request.user.profile == product.seller

#         context = {
#             'product': product,
#             'conversation_id': conversation_id,
#             'user_is_seller': user_is_seller
#         }
#         return render(request, 'components/single_house_view.html', context)
#     except Listing.DoesNotExist:
#         messages.error(request, f'Invalid UID {id} was provided for listing')
#         return redirect('home')





  






        
@method_decorator(login_required, name='dispatch')
class multistepformsubmission(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = 'main/owner/multistep.html'
    form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm,RentalConditionsForm,RulesAndPreferencesForm,ImageForm]
    
    
    def done(self, form_list, **kwargs):
        
        form_data = [form.cleaned_data for form in form_list]
        seller = self.request.user.profile 
        listing = Listing(house_kind = form_data[0]['house_kind'], address = form_data[0]['address'],
                          price = form_data[0]['price'], available_start = form_data[0]['available_start'],
                          available_end = form_data[0]['available_end'] , 
                          minimum_rental_period = form_data[0]['minimum_rental_period'],
                          maximum_rental_period = form_data[0]['maximum_rental_period'],
                          seller=seller )
        
        listing.save()
        
        listing_space = ListingSpaceOverview(house_size = form_data[1]['house_size'],
                                             house_mate_no = form_data[1]['house_mate_no'],
                                            bedroom_size = form_data[1]['bedroom_size'] ,
                                            bedroom_furnished = form_data[1]['bedroom_furnished'],
                                            seller=seller)
        
        listing_space.save()
        listing.listing_space_overview.add(listing_space)
        
        listing_house = ListingHouseArea(kitchen = form_data[2]['kitchen'],
                                        toilet = form_data[2]['toilet'],
                                        bathroom = form_data[2]['bathroom'],
                                        living_room = form_data[2]['living_room'],
                                        garden = form_data[2]['garden'],
                                        seller=seller)
        
        listing_house.save()
        listing.listing_house_area.add(listing_house)
        
        listing_amenities = ListingHouseAmenities(
            bed = form_data[3]['bed'],
            wifi = form_data[3]['wifi'],
            desk = form_data[3]['desk'],
            living_room_furnished = form_data[3]['living_room_furnished'],
            seller=seller
        )
        
        listing_amenities.save()
        listing.amenities.add(listing_amenities)
        
        rental_condition = RentalConditions(
            contract = form_data[4]['contract'],
            cancellation = form_data[4]['cancellation'],
            price = form_data[4]['price'],
            utility_costs = form_data[4]['utility_costs'],
            seller=seller
        )
        
        rental_condition.save()
        listing.rental_condtion.add(rental_condition)
        
        rules_preferences = RulesAndPreferences(
            gender =  form_data[5]['gender'],
            minimum_age = form_data[5]['minimum_age'],
            maximum_age = form_data[5]['maximum_age'],
            tenant = form_data[5]['tenant'],
            proof = form_data[5]['proof'],
            seller=seller
        )
        
        rules_preferences.save()
        listing.rules_and_preferences.add(rules_preferences)
        
        images = Image(
            image1 =  form_data[6]['image1'],
            image2 = form_data[6]['image2'],
            image3 = form_data[6]['image3'],
            image4 = form_data[6]['image4'],
            image5 = form_data[6]['image5'],
            description = form_data[6]['description'],
            seller=seller,
        )
        
        images.save()
        listing.image.add(images)
        # data = Listing.objects.all()
        # return render(self.request, 'main/owner/done.html', {'data': data})
        message = messages.info(self.request, "We will give you a reminder when your listing be approved in 24 hours")
        return render(self.request, 'main/owner/done.html', {'message': message})
            
        # return redirect('master')
    



# def send_email(request):
#     subject = 'Subject here'
#     from_email = 'from@example.com'
#     to_email = ['to@example.com']
    
#     # Load the HTML template
#     html_template = get_template('email_template.html')
#     context = {'variable1': 'value1', 'variable2': 'value2'}
#     html_content = html_template.render(Context(context))

#     # Create the email message
#     email_message = EmailMultiAlternatives(subject, '', from_email, to_email)
#     email_message.attach_alternative(html_content, "text/html")
#     email_message.send()
    
    
    
# def review_view(request):
    # if request.method == 'GET':
    #     form = ReviewForm(request.GET)
    #     if form.is_valid():
    #         review_text = form.cleaned_data['review_text']
    #         rating = form.cleaned_data['rating']
    #         # Perform further processing with the submitted data
            
    #         review = Review.objects.create(
    #             reviewer=request.user,
    #             comment=review_text,
    #             rating=rating,
    #             created_at=datetime.datetime.now()
    #         )
            
    #         return redirect('single_house_view', {'review':review})
            
    # else:
    #     form = ReviewForm()
    # if request.method == "GET":
    #     list_id = request.GET.get('list_id')
    #     listing = Listing.objects.get(id=list_id)
    #     review_text = request.GET.get('review_text')
    #     rating = request.GET.get('rating')
    #     reviewer = request.user.profile
    #     Review(reviewer=reviewer, listing=listing, review_text=review_text,rating=rating).save()
    #     render(request, 'single_house_view', id=list_id)
    
# def review_view(request):
#     if request.method == "GET":
#         list_id = request.GET.get('list_id')
#         review_text = request.GET.get('review_text')
#         rating = request.GET.get('rating')
        
#         try:
#             listing = Listing.objects.get(id=list_id)
#         except Listing.DoesNotExist:
#             return HttpResponse("Listing does not exist.")  # Or you can handle the error differently
            
#         reviewer = request.user.profile
#         Review.objects.create(reviewer=reviewer, listing=listing, review_text=review_text, rating=rating)
        
#         return redirect('single_house_view', id=list_id)
    
    
        
        

    
def search(request):
    res = Listing.objects.order_by('-created')

    keywords = request.GET.get('keywords', "")
    city = request.GET.get('city', "")
    state = request.GET.get('state', "")
    listing_type = request.GET.get('listing_type', 0)
    min_sqft = request.GET.get('sqft', 0)
    max_price = request.GET.get('price', Decimal(10000000))
    min_bedrooms = request.GET.get('bedrooms', 0)
    min_bathrooms = request.GET.get('bathrooms', 0)

    if not min_sqft:
        min_sqft = 0
    if not max_price:
        max_price = 1000000000
    if not min_bedrooms:
        min_bedrooms = 0
    if not min_bathrooms:
        min_bathrooms = 0

    queryset_list = res.filter(
        (Q(description__icontains=keywords) |
         Q(title__icontains=keywords)),
        address__city__icontains=city,
        bedrooms__gte=min_bedrooms,
        bathrooms__gte=min_bathrooms,
        sqft__gte=min_sqft,
        price__lte=max_price,
    )

    try:
        if isinstance(int(listing_type), int):
            queryset_list = queryset_list.filter(listing_type=listing_type)
    except Exception:
        pass

    try:
        if isinstance(int(state), int):
            queryset_list = queryset_list.filter(address__state=state)
    except Exception:
        pass

    context = {
        'states': State.objects.all(),
        'list_types': ListingType.objects.all(),
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/_partials/_search.html', context)
    
    
    
    
    
    
def edit_listing_view(request):
    return render(request, 'main/owner/edit_listing.html')


    
    
    
    
    
    
    
    
    
    
    
def payement(request):
    if request.method == 'POST':
        user_listings = Listing.objects.filter(seller=request.user.profile)
        # user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm()
        location_form = LocationForm()
        
        
        return render(request, 'includes/payemnts.html', {'user_form': user_form, 
                                                      'profile_form': profile_form,
                                                    #   'location_form': location_form, 'user_listings': user_listings
                                                    })
        
    
    elif request.method == 'GET':
        user_listings = Listing.objects.filter(seller=request.user.profile)
        # user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)
        
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Profile Updated successfully!')
            
        else:
            messages.error(request, 'Error updating profile')

        return render(request, 'includes/payemnts.html', {'user_form': user_form, 'profile_form': profile_form, 
                                                    #   'location_form': location_form, 'user_listings': user_listings, 
                                                    })
        

def owner_listings(request):
    return render(request, 'main/owner/owner-listings.html')





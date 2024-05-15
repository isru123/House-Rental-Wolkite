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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from geopy.geocoders import Nominatim
from users.models import Profile
from message.models import Conversation
from paymnet.models import Payment

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
    AddressOfListing,
    Upload,

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
    DocumentForm,
    UploadForm,
)




def main_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    
    
    return render(request, 'main/homepage/home.html',  {'listing_filter': listing_filter,
                                            })



        
        
            
    
            
        # return render(request, 'search_results.html', {'listings': listings})
def master_view(request):
    all_listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=all_listings)
    
    filtered_listings = listing_filter.qs  # Use the filtered queryset from the filter

    if request.method == 'GET':
        address_query = request.GET.get('address')
        
        if address_query:
            # Apply additional filtering based on address query
            filtered_listings = filtered_listings.filter(address__icontains=address_query)
    
    # Fetch related data using prefetch_related
    filtered_listings = filtered_listings.prefetch_related(
        'rules_and_preferences',
        'amenities',
        'listing_space_overview',
        'listing_house_area',
        'rental_condition',
        'image',
    )
    
    return render(request, 'main/major/master.html', {
        'listing_filter': listing_filter,
        'filtered_listings': filtered_listings
    })

   
   
   
   

def detail_list_view(request):
    return render(request, 'components/detail_list_view.html')



def about_view(request):
    return render(request, 'users/about.html')

 
def owner_view(request):
    return render(request, 'main/owner/first.html')


def dashboard_view(request):
    profile = request.user.profile
    listings = Listing.objects.filter(seller=profile)
    pending_listing = Listing.objects.filter(seller=profile, approved=False)
    accepted_listings = Listing.objects.filter(seller=profile, approved=True)
    booking_requests = Upload.objects.filter(listing__seller=profile)
    accepted_requests = Upload.objects.filter(listing__seller=profile, status='Accepted')
    rejected_requests = Upload.objects.filter(listing__seller=profile, status='Rejected')
   
    total_listings = listings.count()
    pendings = pending_listing.count()
    accepted_listings = accepted_listings.count()
    booking_requests = booking_requests.count()
    accepted_requests = accepted_requests.count()
    rejected_requests = rejected_requests.count()
   
    context = {
        'total_listings': total_listings,
        'pendings':pendings,
        'accepted_listings':accepted_listings,
        'booking_requests':booking_requests,
        'accepted_requests':accepted_requests,
        'rejected_requests':rejected_requests,
    }
    return render(request, 'main/owner/dashboard.html', context)




def owner_second_view(request):
    message = None
    address = AddressOfListing.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            listing = get_object_or_404(Listing, id=id)
            document = form.save(commit=False)
            document.seller = listing.seller  # Assign the seller object to the document
            document.listing = listing  # Assign the listing object to the document
            document.save()
                
            message = messages.success(request, 'You successfully submitted.')
            return redirect('second')
            
    else:
        form = DocumentForm()
    
    return render(request, 'main/owner/second.html', {'form': form,'message':message,'showaddress': address})
    







def map_view(request, id):
    
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
    
    listing = get_object_or_404(Listing, id=id)
    context = {
        'listing': listing,
        'opencage_api_key': settings.OPENCAGE_API_KEY,
    }
    
    return render(request, 'main/major/location.html', context)




def my_view(request, id):
    mss = None
    message = None
    address = AddressOfListing.objects.all()
    try:
        
        listing = get_object_or_404(Listing, id=id)
    
    except Listing.DoesNotExist:
        messages.error(request, "First, you need to create a listing.")
        return redirect('multistepformsubmission')
    
    if request.method == 'POST':
        try:
        
            address = request.POST.get('addloc')
            listing = Listing.objects.get(pk=id)  # Replace `listing_id` with the appropriate value
            
            address_listing = get_object_or_404(AddressOfListing, Address=address)
        
            latitude = address_listing.lat
            longitude = address_listing.long
            
            listing.latitude = latitude
            listing.longitude = longitude
            
            listing.address = address
            listing.save()
            messages.success(request= 'we will give you a remainder when the listing is approved')
            return redirect('main:upload_file' , id=listing.id)
            
        
            
        except Exception as e:
            print(e)
            messages.success(
                request, 'Successfully submitted address'
            )
            
    else:
        
        listing = Listing.objects.get(pk=id) 
    
    return render(request, 'main/major/my_form.html', {'showaddress': address, 'listing_id': listing.id})
    




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
        request_is_approved = Upload.objects.filter(tenant=request.user.profile, listing=listing , status= 'Accepted')
        user_has_sent_request = Upload.objects.filter(tenant=request.user.profile, listing=listing).exists()
        
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
                                        'filtered_listings':filtered_listings, 'conversation_id':conversation_id,
                                        'reviews':reviews,'review_form': review_form,'latitude': latitude,
                                        'longitude': longitude, 'user_has_sent_request':user_has_sent_request,'request_is_approved':request_is_approved})
    except Listing.DoesNotExist:
        messages.error(request, f'Invalid UID {id} was provided for listing')
        # return redirect('home')
        return redirect('new', product_id=listing.id, conversation_id=conversation_id)





def upload(request,id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        try:
            
            if form.is_valid():
                # move_in_date = form.cleaned_data['move_in_date']
                # move_out_date = form.cleaned_data['move_out_date']
                # print(listing.available_start)
                # if is_request_valid(move_in_date, move_out_date,listing.available_start):
                    
                upload = form.save(commit=False)
                user_profile = Profile.objects.get(user=request.user)
                upload.tenant = user_profile
                upload.listing = listing  # Assign the listing object
                existing_request = Upload.objects.filter(tenant=user_profile, listing=listing).exists()
                if existing_request:
                    
    
                    form.add_error(None, "You have already made a request for this listing.")
                else:
    
                    upload.tenant = user_profile
            
                    upload.save()
                    messages.success(request, 'You have successfully sent the Documents')
                    return redirect('message:new', product_id=listing.id)
                
                # else:
                #     messages.warning(request, 'You have to Correct The Dates')
        
        except Exception as e:
            
            
            messages.warning(request, 'You have to upload the Neccessary files!')
            print(e)
    else:
        form = UploadForm()
    return render(request, 'payment/upload.html', {'form': form, 'listing': listing})



from paymnet.models import Booking
#   all_bookings = Booking.objects.filter(tenant=request.user)


def bookings_made(request):
    profile = request.user.profile
    
    
    
    bookings = Booking.objects.filter(house__seller=profile)
    
    
    
    page = request.GET.get('page', 1)

    paginator = Paginator(bookings, 7)
    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        bookings = paginator.page(1)
    except EmptyPage:
        bookings = paginator.page(paginator.num_pages)
    
    
    return render(request, 'main/owner/bookings.html', {'bookings': bookings})
  
  
  
  
def payment_made(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Filter payments where the logged-in user is either the payer or the recipient
    A = Payment.objects.filter(payer=request.user) | Payment.objects.filter(recipient=request.user)
    all_bookings = Booking.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(A, 7)
    try:
        A = paginator.page(page)
    except PageNotAnInteger:
        A = paginator.page(1)
    except EmptyPage:
        A = paginator.page(paginator.num_pages)
    # Pass the filtered payments to the template
  
  

    return render(request,'main/owner/payments.html', {'payments': A, 'all_bookings':all_bookings})
 
 
def booking_requests(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user=request.user)
    U = Upload.objects.filter(listing__seller=profile, status='Pending')
    if request.method == "POST":
        search = request.POST.get("search")
        # seller = seller.user.username
        # seller = request.user.profile 
        U = Upload.objects.filter(tenant__user__username__icontains=search, status='Pending')
    
    page = request.GET.get('page', 1)

    paginator = Paginator(U, 7)
    try:
        U = paginator.page(page)
    except PageNotAnInteger:
        U = paginator.page(1)
    except EmptyPage:
        U = paginator.page(paginator.num_pages)

    return render(request,'main/owner/booking_requests.html', {'requests': U})



def messages_view(request):
    profile = request.user.profile
    conversations = Conversation.objects.filter(item__seller=profile)
    context = {
        'conversations': conversations
    }
    return render(request, 'main/owner/messages.html', context)






def identity_page(request):
    # Your identity page view logic here
    return render(request, 'payment/identity.html') 



def review_view(request):
    obj = Review.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'ratings/main.html', context)




def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Review.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})








  






        
@method_decorator(login_required, name='dispatch')
class multistepformsubmission(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = 'main/owner/multistep.html'
    form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm,RulesAndPreferencesForm,ImageForm]
    
    
    def done(self, form_list, **kwargs):
        
        form_data = [form.cleaned_data for form in form_list]
        seller = self.request.user.profile 
        # address = kwargs.get('address')
        
        listing = Listing(
                          house_kind = form_data[0]['house_kind'],
                          price = form_data[0]['price'], available_start = form_data[0]['available_start'],
                         
                          id_photo = form_data[0]['id_photo'],
                          house_map = form_data[0]['house_map'],
                          seller=seller )
        # Get the address from the form data and update the existing listing
        
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
        
        # rental_condition = RentalConditions(
        #     # contract = form_data[4]['contract'],
        #     # cancellation = form_data[4]['cancellation'],
        #     # price = form_data[4]['price'],
        #     # utility_costs = form_data[4]['utility_costs'],
        #     seller=seller
        # )
        
        # rental_condition.save()
        # listing.rental_condtion.add(rental_condition)
        
        rules_preferences = RulesAndPreferences(
            gender =  form_data[4]['gender'],
            minimum_age = form_data[4]['minimum_age'],
            maximum_age = form_data[4]['maximum_age'],
            tenant = form_data[4]['tenant'],
            # proof = form_data[4]['proof'],
            seller=seller
        )
        
        rules_preferences.save()
        listing.rules_and_preferences.add(rules_preferences)
        
        images = Image(
            image1 =  form_data[5]['image1'],
            image2 = form_data[5]['image2'],
            image3 = form_data[5]['image3'],
            image4 = form_data[5]['image4'],
            image5 = form_data[5]['image5'],
            description = form_data[5]['description'],
            seller=seller,
        )
        
        images.save()
        listing.image.add(images)
        listing_id = Listing.objects.get(id=listing.id)
        print(listing_id)
        # data = Listing.objects.all()
        # return render(self.request, 'main/owner/done.html', {'data': data})
        messages.add_message(self.request, messages.INFO, "We will give you a reminder when your listing is approved in 24 hours")
        return redirect( 'main:my-form', id=listing_id)
    
    def form_invalid(self, form):
        messages.info(self.request, "Please fill in all the required fields.")
        return super().form_invalid(form)
    









from django.shortcuts import get_object_or_404, redirect

def delete_listing(request, id):
    # Get the listing object or return a 404 error if it doesn't exist
    listing = get_object_or_404(Listing, id=id)
    
    # Check if the user has permission to delete the listing
    if request.user.profile != listing.seller:
        # You can customize the error message or redirect the user to another page
        messages.error(request, "You don't have permission to delete this listing.")
        return redirect('main:home')  # Redirect the user to the homepage or another appropriate page
    
    # Delete the listing
    listing.delete()
    
    # Optionally, you can add a success message
    messages.success(request, "Listing deleted successfully.")
    
    # Redirect the user to another page, such as the user's profile or homepage
    return redirect('main:owner-listings')  # Redirect the user to the homepage or another appropriate page










            
        # return redirect('master')
    
# def done_view(request):
#     return render(request, 'main/major/done.html')


def is_request_valid(move_in_date, move_out_date, available_start):
    move_in_date = datetime.strptime(move_in_date, '%Y-%m-%d').date() if isinstance(move_in_date, str) else move_in_date
    move_out_date = datetime.strptime(move_out_date, '%Y-%m-%d').date() if isinstance(move_out_date, str) else move_out_date
    available_start = datetime.strptime(available_start, '%Y-%m-%d').date() if isinstance(available_start, str) else available_start

    if (move_in_date >= available_start) and ((move_out_date - move_in_date).days >= 30) and ((move_out_date - move_in_date).days % 30 == 0):
        return True
    return False


from django.contrib import messages

def create_booking(request, id):
    listing = Listing.objects.get(pk=id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            
            booking = form.save(commit=False)
            booking.guest = request.user.profile
            booking.listing = listing
            booking.save()
            messages.success(request, 'Request sent successfully')
            return redirect('booking_confirmation', message='success')
    else:
        form = BookingForm()

    return render(request, 'includes/booking/create.html', {'form': form, 'listing': listing})



def booking_confirmation_view(request):
    
    return render(request, 'includes/booking/booking_confirmation.html')



# def booking_requests(request):
#     booking_requests = Booking.objects.filter(listing__seller=request.user.profile, status='pending')
#     return render(request, 'booking/booking_requests.html', {'booking_requests': booking_requests})



def review_booking_request(request,id):
    booking = Booking.objects.get(pk=id)
    
    if request.method == 'POST':
        if 'accept' in request.POST:
            booking.status = 'accepted'
            booking.save()
            return redirect('booking_requests')
        elif 'reject' in request.POST:
            booking.status = 'rejected'
            booking.save()
            return redirect('booking_requests')

    return render(request, 'booking/review_booking_request.html', {'booking': booking})





def save_listing(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        listing = Listing(address=address)
        listing.save()
        return redirect('success')  # Redirect to a success page

    return render(request, 'form.html')




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
    queryset_list = Listing.objects.order_by('created_at')

    
    address = request.GET.get('address', "")
    price = request.GET.get('price')

    # Convert price to a Decimal if it's a valid number, otherwise use a default value
    if price:
        try:
            max_price = Decimal(price)
        except (ValueError, TypeError):
            max_price = Decimal(10000000)
    else:
        max_price = Decimal(10000000)
        price = ""  # Set an empty string as the default value for the template

    queryset_list = queryset_list.filter(
        address__icontains=address,
        price__lte=max_price,
    )

    # Filter based on the button clicked for price
    price_button = request.GET.get('price_button')
    if price_button == 'low':
        queryset_list = queryset_list.order_by('price')
    elif price_button == 'high':
        queryset_list = queryset_list.order_by('-price')

    # Filter based on the button clicked for address
    address_button = request.GET.get('address_button')
    if address_button == 'asc':
        queryset_list = queryset_list.order_by('address')
    elif address_button == 'desc':
        queryset_list = queryset_list.order_by('-address')

    context = {
        'listing_filter': queryset_list,
        'values': request.GET,
        'price': price  # Include the price variable in the context
    }

    return render(request, 'main/major/master.html', context)
    
    
    
def edit_listing_view(request):
    return render(request, 'main/owner/edit_listing.html')


    





from django.shortcuts import get_object_or_404
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class multistepsubmissionEdit(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = 'main/owner/multistep.html'
    form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm, RentalConditionsForm, RulesAndPreferencesForm, ImageForm]

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        listing_id = self.kwargs.get('listing_id')

        if listing_id:
            listing = get_object_or_404(Listing, id=listing_id)

            if step == '0':
                initial.update({
                    'address': listing.address,
                    'house_kind': listing.house_kind,
                    'price': listing.price,
                    'available_start': listing.available_start,
                    'available_end': listing.available_end,
                })
            elif step == '1':
                listing_space = listing.listing_space_overview.first()
                if listing_space:
                    initial.update({
                        'house_size': listing_space.house_size,
                        'house_mate_no': listing_space.house_mate_no,
                        'bedroom_size': listing_space.bedroom_size,
                        'bedroom_furnished': listing_space.bedroom_furnished,
                    })
            elif step == '2':
                listing_house = listing.listing_house_area.first()
                if listing_house:
                    initial.update({
                        'kitchen': listing_house.kitchen,
                        'toilet': listing_house.toilet,
                        'bathroom': listing_house.bathroom,
                        'living_room': listing_house.living_room,
                        'garden': listing_house.garden,
                    })
            elif step == '3':
                listing_amenities = listing.amenities.first()
                if listing_amenities:
                    initial.update(
                        {
                            'bed':listing_amenities.bed,
                            'wifi':listing_amenities.wifi,
                            'desk':listing_amenities.desk,
                            'living_room_furnished':listing_amenities.living_room_furnished,
                            
                        }
                    )
                
            elif step == '4':
                rental_condition = listing.rental_condtion.first()
                if rental_condition:
                    initial.update(
                        {
                            'contract':rental_condition.contract,
                            'cancellation':rental_condition.cancellation,
                            'price':rental_condition.price,
                            'utility_costs':rental_condition.utility_costs,
                            
                            
                        }
                    )
                
            elif step == '5':
                rules_preferences = listing.rules_and_preferences.first()
                if rules_preferences:
                    initial.update(
                        {
                        'gender':rules_preferences.gender,
                        'minimum_age':rules_preferences.minimum_age,
                        'maximum_age':rules_preferences.maximum_age,
                        'tenant':rules_preferences.tenant,
                        'proof':rules_preferences.proof,
                        }
                        
                    )
                    
            elif step == '6':
                images = listing.image.first()
                if images:
                    initial.update(
                        {
                            'image1':images.image1,
                            'image2':images.image2,
                            'image3':images.image3,
                            'image4':images.image4,
                            'image5':images.image5,
                            'description':images.description,
                        }
                        
                    )
                
        return initial
    
    

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        seller = self.request.user.profile

        listing_id = self.kwargs.get('listing_id')
        if listing_id:
            listing = get_object_or_404(Listing, id=listing_id)
        else:
            listing = Listing(seller=seller)

        listing.address = form_data[0]['address']
        listing.house_kind = form_data[0]['house_kind']
        listing.price = form_data[0]['price']
        listing.available_start = form_data[0]['available_start']
        listing.available_end = form_data[0]['available_end']
        listing.save()

        # Update or create listing space overview
        listing_space, _ = ListingSpaceOverview.objects.get_or_create(listing=listing)
        listing_space.house_size = form_data[1]['house_size']
        listing_space.house_mate_no = form_data[1]['house_mate_no']
        listing_space.bedroom_size = form_data[1]['bedroom_size']
        listing_space.bedroom_furnished = form_data[1]['bedroom_furnished']
        listing_space.save()

        # Update or create listing house area
        listing_house, _ = ListingHouseArea.objects.get_or_create(listing=listing)
        listing_house.kitchen = form_data[2]['kitchen']
        listing_house.toilet = form_data[2]['toilet']
        listing_house.bathroom = form_data[2]['bathroom']
        listing_house.living_room = form_data[2]['living_room']
        listing_house.garden = form_data[2]['garden']
        listing_house.save()

        # Update or create listing amenities
        listing_amenities, _ = ListingHouseAmenities.objects.get_or_create(listing=listing)
        listing_amenities.bed = form_data[3]['bed']
        listing_amenities.wifi = form_data[3]['wifi']
        listing_amenities.desk = form_data[3]['desk']
        listing_amenities.living_room_furnished = form_data[3]['living_room_furnished']
        listing_amenities.save()

        # Update or create rental conditions
        rental_condition, _ = RentalConditions.objects.get_or_create(listing=listing)
        rental_condition.contract = form_data[4]['contract']
        rental_condition.cancellation = form_data[4]['cancellation']
        rental_condition.price = form_data[4]['price']
        rental_condition.utility_costs = form_data[4]['utility_costs']
        rental_condition.save()

        # Update or create rules and preferences
        rules_preferences, _ = RulesAndPreferences.objects.get_or_create(listing=listing)
        rules_preferences.gender = form_data[5]['gender']
        rules_preferences.minimum_age = form_data[5]['minimum_age']
        rules_preferences.maximum_age = form_data[5]['maximum_age']
        rules_preferences.tenant = form_data[5]['tenant']
        rules_preferences.proof = form_data[5]['proof']
        rules_preferences.save()

        # Update or create images
        images, _ = Image.objects.get_or_create(listing=listing)
        images.image1 = form_data[6]['image1']
        images.image2 = form_data[6]['image2']
        images.image3 = form_data[6]['image3']
        images.image4 = form_data[6]['image4']
        images.image5 = form_data[6]['image5']
        images.description = form_data[6]['description']
        images.save()

        messages.add_message(self.request, messages.INFO, "We will give you a reminder when your listing is approved in 24 hours")
        return render(self.request, 'main/owner/done.html', {'listing_id': listing.id})

    def form_invalid(self, form):
        messages.info(self.request, "Please fill in all the required fields.")
        return super().form_invalid(form)
    
    
    
    
    
    
    
    
    
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
    profile = request.user.profile
    L = Listing.objects.filter(seller=profile)
    if request.method == "POST":
        search = request.POST.get("search")
        # seller = seller.user.username
        # seller = request.user.profile 
        L = Listing.objects.filter(user__house_kind__icontains=search)
        
    for listing in L:
        if listing.approved:
            listing.status = "Approved"
        else:
            listing.status = "Pending"
            
            
   
    
    page = request.GET.get('page', 1)

    paginator = Paginator(L, 7)
    try:
        L = paginator.page(page)
    except PageNotAnInteger:
        L = paginator.page(1)
    except EmptyPage:
        L = paginator.page(paginator.num_pages)

    # return render(request, 'adminApp/approve-owner.html',  {'listing':L})
    return render(request, 'main/owner/owner-listings.html',  {'listing':L})


import uuid
from django.http import Http404

def delete_upload(request, request_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    try:
        upload = Upload.objects.get(id=request_id)
    except Upload.DoesNotExist:
        raise Http404("Upload object not found.")
    
    upload.delete()
    messages.success(request, 'The Request has been deleted successfully.')
    return redirect('message:ask')


# def delete_upload(request, id):
#     upload = get_object_or_404(Upload, id=id)
#     if request.method == 'POST':
#         upload.delete()
#         messages.success(request, 'The upload has been deleted successfully.')
#         return redirect('message:ask')
#     else:
#         return redirect('message:ask')


def approve_tenant_request(request, listing_id):
    
    upload = Upload.objects.filter(listing_id=listing_id).first()
    
    upload.status = 'Accepted'
    upload.save() 
 
    
    messages.success(request, 'Request Approved!')
    return redirect('main:Request')
    
def reject_tenant_request(request, listing_id):
    
    upload = Upload.objects.get(listing_id=listing_id)
    
    upload.status ='Rejected'
    upload.save()
    
    messages.info(request, 'You rejected booking request')
    return redirect('main:Request')





# subject = 'Listing Approved'
    # from_email = settings.EMAIL_HOST_USER
    # to_email = ['lema2127@gmail.com']
    
    # messages.info(request, 'Welcome To Housing At Wolkite')
    # messages.success(request, 'Listing has been verified.')
    
    # html_content = render_to_string('adminApp/email_template.html', {'variable1': 'Welcome To Housing At Wolkite', 'variable2': 'Listing has been verified.'})
    # # Create the email message
    # email_message = EmailMultiAlternatives(subject, body=None, from_email=from_email, to=to_email)
    # email_message.attach_alternative(html_content, "text/html")
    # email_message.send()
    # Redirect to a success page or back to the listing details page

def upload_documents(request):
    message = None
    address = AddressOfListing.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = messages.success(request, 'You Successfully submited')
    else:
        form = DocumentForm()
    
    return render(request, 'main/owner/second.html', {'form': form,'message':message,'showaddress': address})





def search_listings(request):
    # Retrieve search query parameters
    keyword = request.GET.get('keyword')  # Search term entered by the user
    house_kind = request.GET.get('house_kind')
    gender = request.GET.get('gender')
    tenant_type = request.GET.get('tenant_type')
    
    # Create an initial queryset of all listings
    queryset = Listing.objects.all()
    
    # Apply filters based on the search criteria
    if keyword:
        queryset = queryset.filter(description__icontains=keyword)
    
    if house_kind:
        queryset = queryset.filter(house_kind=house_kind)
        
    if gender:
        queryset = queryset.filter(rules_and_preferences__gender=gender)
        
    if tenant_type:
        queryset = queryset.filter(rules_and_preferences__tenant=tenant_type)
    
    return render(request, 'search_results.html', {'listings': queryset})



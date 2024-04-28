from django.urls import path
from .views import main_view,detail_list_view,owner_view,dashboard_view,single_house_view,master_view,owner_second_view
from .views import multistepformsubmission,payement,map_view,edit_listing_view,search,owner_listings,review_view,rate_image,my_view
from .autocomplete import AddressAutocomplete

urlpatterns = [
     path("", main_view, name="home"), 
     path('owner/', owner_view , name='owner'),
     path('master/', master_view, name='master'),
     path('dashboard_owner/', dashboard_view, name='dashboard_owner'),
     # path('listing/', list_view, name='listing'),
     path('payement/', payement, name='payement'),
     path('second/', owner_second_view , name='second'),
     path('detail-view/', detail_list_view, name='detail_product_view'), 
     path('single_house_view/<str:id>/', single_house_view , name='single_house_view'),
     
     # path('listing/<str:id>/like/', like_listing_view , name='like_listing'),
     path('multistepformsubmission/', multistepformsubmission.as_view(), name='multistepformsubmission'),
     path('edit_listing/<str:id>/', edit_listing_view , name='edit_listing'),
     # path('review/', review_view , name='review'),
     path('map/<str:id>/', map_view, name='map'),
     path('search', search, name='search'),
     path('owner-listings/', owner_listings , name='owner-listings'),
     path('address-autocomplete/', AddressAutocomplete.as_view(), name='address-autocomplete'),
     path('my-form/', my_view, name='my-form'),
     # path('booking/<str:id>/', booking , name='booking'),
    
    
]







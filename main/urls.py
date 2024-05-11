from django.urls import path
from .views import main_view,detail_list_view,owner_view,dashboard_view,single_house_view,master_view,owner_second_view,upload,identity_page
from .views import multistepformsubmission,multistepsubmissionEdit,reject_tenant_request,approve_tenant_request,payement,map_view,messages_view,booking_requests,edit_listing_view,search,owner_listings,review_view,rate_image,my_view,create_booking,booking_confirmation_view
from .autocomplete import AddressAutocomplete
app_name = 'main'
urlpatterns = [
     path("", main_view, name="home"), 
     path('owner/', owner_view , name='owner'),
     path('master/', master_view, name='master'),
     path('dashboard_owner/', dashboard_view, name='dashboard_owner'),
     # path('listing/', list_view, name='listing'),
     path('payement/', payement, name='payement'),
     path('second/<str:id>/', owner_second_view , name='second'),
     path('detail-view/', detail_list_view, name='detail_product_view'), 
     path('single_house_view/<str:id>/', single_house_view , name='single_house_view'),
     path('upload/<str:id>/', upload, name='upload'),
     path('identity/',identity_page, name='identity-page'),  # Replace 'identity-page' with your desired URL name
    

     # path('listing/<str:id>/like/', like_listing_view , name='like_listing'),
     path('multistepformsubmission', multistepformsubmission.as_view(), name='multistepformsubmission'),
     path('multistepsubmissionEdit/', multistepsubmissionEdit.as_view(), name='multistepsubmissionEdit'),
     path('edit_listing/<str:id>/', edit_listing_view , name='edit_listing'),
     # path('review/', review_view , name='review'),
     path('map/<str:id>/', map_view, name='map'),
     path('search/', search, name='search'),
     path('owner-listings/', owner_listings , name='owner-listings'),
     path('booking-requests/', booking_requests , name="Request"),
     path('address-autocomplete/', AddressAutocomplete.as_view(), name='address-autocomplete'),
     path('my-form/<str:id>/', my_view, name='my-form'),
     path('messages_board/', messages_view , name="MIDI"),
     # path('done/', done_view , name='done'),
     # path('second/', upload_documents, name='upload_documents'),
     path('approve-tenant-request/<uuid:listing_id>/', approve_tenant_request, name='approve_tenant_request'),
     path('reject-tenant-request/<uuid:listing_id>/', reject_tenant_request , name='reject_tenant_request'),
     path('booking/<str:id>/', create_booking , name='booking'),
     path('booking_confirmation/', booking_confirmation_view , name='booking_confirmation'),
    
    
]







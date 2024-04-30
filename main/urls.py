from django.urls import path
from .views import main_view,detail_list_view,owner_view,dashboard_view,single_house_view,master_view,owner_second_view, upload,identity_page
from .views import multistepformsubmission,payement,edit_listing_view


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
     path('upload/', upload, name='upload'),
         path('identity/',identity_page, name='identity-page'),  # Replace 'identity-page' with your desired URL name


     # path('listing/<str:id>/like/', like_listing_view , name='like_listing'),
     path('multistepformsubmission/', multistepformsubmission.as_view(), name='multistepformsubmission'),
     path('edit_listing/<str:id>/', edit_listing_view , name='edit_listing'),

     # path('location/', map_view , name='map_view'),
     # path('search', search, name='search'),
     # path('booking/<str:id>/', booking , name='booking'),
    
]







from django.urls import path
<<<<<<< HEAD
from .views import main_view,detail_list_view,owner_view,dashboard_view,listing_view,multistepformsubmission,message
=======
from .views import main_view,detail_list_view,owner_view,dashboard_view,listing_view,multistepformsubmission,single_house_view,master_view,like_listing_view,owner_second_view
>>>>>>> 2293d66db9847ce3491b3a05c0e2ecab94a3eed7



urlpatterns = [
     path("", main_view, name="home"), 
     path('owner/', owner_view , name='owner'),
     path('master/', master_view, name='master'),
     path('dashboard/', dashboard_view, name='dashboard'),
     path('listing/', listing_view, name='listing'),
     path('second/', owner_second_view , name='second'),
     path('detail-view/', detail_list_view, name='detail_product_view'), 
<<<<<<< HEAD
     path('message/', message, name='message'),

     path('multistepformsubmission/', multistepformsubmission, name='multistepformsubmission') 
=======
     path('multistepformsubmission/', multistepformsubmission.as_view(), name='multistepformsubmission'),
     path('single_house_view/', single_house_view , name='single_house_view'),
     path('listing/<str:id>/like/', like_listing_view , name='like_listing'),
>>>>>>> 2293d66db9847ce3491b3a05c0e2ecab94a3eed7
]







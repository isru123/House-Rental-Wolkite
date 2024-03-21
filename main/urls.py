from django.urls import path
from .views import main_view,detail_list_view,owner_view,dashboard_view,single_house_view,master_view,like_listing_view,owner_second_view

from .views import list_view


urlpatterns = [
     path("", main_view, name="home"), 
     path('owner/', owner_view , name='owner'),
     path('master/', master_view, name='master'),
     path('dashboard/', dashboard_view, name='dashboard'),
     path('listing/', list_view, name='listing'),
     path('second/', owner_second_view , name='second'),
     path('detail-view/', detail_list_view, name='detail_product_view'), 
     path('single_house_view/', single_house_view , name='single_house_view'),
     path('listing/<str:id>/like/', like_listing_view , name='like_listing'),
     # path('multistepformsubmission/', multistepformsubmission.as_view(), name='multistepformsubmission'),
     # path('space_overview/', SpaceOverview   , name='listing_space_overview'),
]







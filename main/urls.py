from django.urls import path
from .views import main_view,detail_list_view,owner_view,dashboard_view,single_house_view,master_view,owner_second_view
from .views import multistepformsubmission,payement


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
     #path('location/', map_view , name='map_view'),
     # path('space_overview/', SpaceOverview   , name='listing_space_overview'),
]







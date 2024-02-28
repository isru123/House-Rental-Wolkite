from django.urls import path
from .views import main_view,detail_list_view,owner_view,dashboard_view,listing_view


# file_storage = FileSystemStorage(location= 'media/listings')

urlpatterns = [
     path("", main_view, name="home"), 
     path('owner/', owner_view , name='owner'),
     path('dashboard/', dashboard_view, name='dashboard'),
     path('listing/', listing_view, name='listing'),
     path('detail-view/', detail_list_view, name='detail_product_view'),  
]







from django.urls import path
from .views import main_view, master_view,detail_list_view


# file_storage = FileSystemStorage(location= 'media/listings')

urlpatterns = [
     path("", main_view, name="home"), 
     path('master/', master_view , name='master'),
     path('detail-view/', detail_list_view, name='detail_product_view'),
]







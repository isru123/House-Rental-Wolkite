from django.urls import path
from django.core.files.storage import FileSystemStorage
from .views import main_view, master_view


# file_storage = FileSystemStorage(location= 'media/listings')

urlpatterns = [
     path("", main_view, name="home"), 
     path('master/', master_view , name='master'),
     # path('listing/<str:id>/', listing_view, name='listing'),
]







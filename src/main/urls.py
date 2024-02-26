from django.urls import path
from .views import main_view, master_view

urlpatterns = [
     path("", main_view, name="home"), 
     path('master/', master_view , name='master'),
     
]





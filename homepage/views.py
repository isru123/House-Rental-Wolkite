
# Create your views here.
from django.shortcuts import render
from main.models import Listing

def index(request):
    listings = Listing.objects.all()
    return render(request, 'homepage/main/home.html',{'listings': listings})



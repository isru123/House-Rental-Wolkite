from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm
from importlib import reload


def main_view(request):
    return render(request, 'main/homepage/home.html', {'name': 'home'})



@login_required
def master_view(request):
    listings = Listing.objects.all()
    return render(request, 'main/major/master.html', {'listings': listings})


def detail_list_view(request):
 
 return render(request, 'components/detail_list_view.html')







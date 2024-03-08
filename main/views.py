from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Listing
from .forms import ListingForm
from .forms import ListingSpaceOverviewForm,ListingHouseAreaForm,ListingHouseAmenitiesForm,RentalConditionsForm, RulesAndPreferencesForm
from django.core.files.storage import DefaultStorage
from importlib import reload
from formtools.wizard.views import SessionWizardView


def main_view(request):
    return render(request, 'main/homepage/home.html', {'name': 'home'})



@login_required
def master_view(request):
    listings = Listing.objects.all()
    return render(request, 'main/major/master.html', {'listings': listings})


def detail_list_view(request):
    return render(request, 'components/detail_list_view.html')

 
def owner_view(request):
    return render(request, 'main/owner/first.html')


def dashboard_view(request):
    return render(request, 'main/owner/dashboard.html')

def listing_view(request):
    return render(request, 'main/owner/listing.html')



class multistepformsubmission(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = 'main/owner/listing.html'
    form_list = [ListingForm, ListingSpaceOverviewForm, ListingHouseAreaForm, ListingHouseAmenitiesForm,RentalConditionsForm,RulesAndPreferencesForm]
    
    
    def done(self, form_list, **kwargs):
        return HttpResponse('form submitted!')
    
    






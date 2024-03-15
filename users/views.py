from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View

from .forms import UserForm,ProfileForm,LocationForm
from main.models import Listing,LikedListing

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('master')
            else:
                messages.error(request, f'error occured during trying to login')
        else:
             messages.error(request, f'error occured during trying to login')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'users/login.html', {'login_form': login_form})



@login_required
def logout_view(request):
    logout(request)
    return redirect('home')




class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'users/register.html', {'register_form': register_form})
    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f'User { user.username}  registered successfully')
            return redirect('master')
        else:
             messages.error(request, f'error occured during tying to register')
             return render(request, 'users/register.html', {'register_form': register_form})
        


        
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm()
        location_form = LocationForm()
        
        
        return render(request, 'users/profile.html', {'user_form': user_form, 
                                                      'profile_form': profile_form,
                                                      'location_form': location_form, 'user_listings': user_listings, 'user_liked_listings': user_liked_listings})
        
    
    def post(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)
        
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Profile Updated successfully!')
            
        else:
            messages.error(request, 'Error updating profile')

        return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form, 
                                                      'location_form': location_form, 'user_listings': user_listings,'user_liked_listings': user_liked_listings })
        




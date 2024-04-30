from django.shortcuts import render,redirect
from users.models import Profile,Location
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .forms import AdminProfileForm
from users.forms import LocationForm,UserForm
from django.db import models
from django.conf import settings
from main.models import Listing
# Create your views here.


def admin_view(request):
    return render(request, 'adminApp/adminHome.html')


    
def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    total_verified_owner = Profile.objects.filter(userType="Owner", verified=True).count()
    total_unverified_owner = Profile.objects.filter(userType="Owner", verified=False).count()

    total_verified_admin = Profile.objects.filter(userType="Admin", verified=True).count()
    total_unverified_admin = Profile.objects.filter(userType="Admin", verified=False).count()

    # available_house = House.objects.filter(status="Available").count()
    # booked_house = House.objects.filter(status="Booked").count()

    # customer_request = BookingRequest.objects.filter(status="Pending").count()

    # my_house = House.objects.filter(user=UserProfile.objects.get(user=request.user)).count()
    # my_available_house = House.objects.filter(user=UserProfile.objects.get(user=request.user), status="Available").count()

    # my_booking = BookingRequest.objects.filter(user=UserProfile.objects.get(user=request.user)).count()

    Dict = {
        "total_verified_owner":total_verified_owner,
        "total_unverified_owner":total_unverified_owner,
        "total_verified_admin":total_verified_admin,
        "total_unverified_admin":total_unverified_admin,
        # "available_house":available_house,
        # "booked_house":booked_house,
        # "customer_request":customer_request,

        # "my_house": my_house,
        # "my_available_house":my_available_house,

        # "my_booking":my_booking
    }
    return render(request, 'adminApp/board.html',Dict)



def approve_owner_view(request):
    return render(request, 'adminApp/approve-owner.html')

def manage_customer_view(request):
    return render(request, 'adminApp/manage-customer.html')

def ViewUser(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    u = Profile.objects.get(id=id)

    return render(request, 'adminApp/view_user.html',{'user':u})


def DeleteUser(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    u = User.objects.get(id=id)
    u.delete()
    return redirect('all-user')


def add_admin_view(request):
    if request.method == 'GET':
        user_form = UserForm()
        profile_form = AdminProfileForm()
        location_form = LocationForm()
    
        return render(request, 'adminApp/add-admin.html', {'user_form':user_form,'profile_form': profile_form, 'location_form': location_form})
    
    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = AdminProfileForm(request.POST, request.FILES)
        location_form = LocationForm(request.POST)
        
        return render(request, 'adminApp/add-admin.html', {'user_form':user_form,'profile_form': profile_form, 'location_form': location_form})

        
def Approve_listing(request):
    L = Listing.objects.filter(approved=False).exclude(user=request.user)
    if request.method == "POST":
        search = request.POST.get("search")
        seller = seller.user.username
        # seller = request.user.profile 
        L = Listing.objects.filter(user__seller__icontains=search, approved=False).exclude(user=request.user)
    
    page = request.GET.get('page', 1)

    paginator = Paginator(L, 10)
    try:
        L = paginator.page(page)
    except PageNotAnInteger:
        L = paginator.page(1)
    except EmptyPage:
        L = paginator.page(paginator.num_pages)

    return render(request, 'adminApp/approve-owner.html',  {'listing':L})

  
        
 



def AllUser(request):
    u = Profile.objects.filter(verified=True).exclude(user=request.user)
    if request.method == "POST":
        search = request.POST.get("search")
        u = Profile.objects.filter(user__first_name__icontains=search, verified=True).exclude(user=request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(u, 10)
    try:
        u = paginator.page(page)
    except PageNotAnInteger:
        u = paginator.page(1)
    except EmptyPage:
        u = paginator.page(paginator.num_pages)
    return render(request, 'adminApp/all-user.html', {'user':u})


def AddAdmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        DOB = request.POST.get('dob')
        profile_pic = request.FILES.get('pic')
        gender=request.POST.get('gender')
        address= request.POST.get('address')
        
        if pass1!=pass2:
            msg='Password should be same.'
            return render(request,'adminApp/add-admin.html',{'msg':msg})
        if len(contact)!=10:
            msg='Contact should be 10 digit.'
            return render(request,'adminApp/add-admin.html',{'msg':msg})
        try:
            user=User.objects.create_user(
                username=username,
                email=email,
                password=pass1,
                first_name=first_name,
                last_name=last_name
                )
        except:
            msg='Usename already exist.'
            return render(request,'adminApp/add-admin.html',{'msg':msg})
        Profile.objects.create(
            user=user,
            profilePicture=profile_pic,
            contact_No=contact,
            address=address,
            gender=gender,
            DOB=DOB,
            userType="Admin"
            )
        return redirect('all-user')
    return render(request, 'adminApp/add-admin.html')


# def Profile(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     return render(request,'profile.html')








        
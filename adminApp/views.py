from django.shortcuts import render,redirect,get_object_or_404
from users.models import Profile,Location
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .forms import AdminProfileForm
from users.forms import LocationForm,UserForm
from django.db import models
from django.conf import settings
from main.models import Listing,Image
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from main.forms import ListingForm
from django.utils.translation import gettext as _
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



# def approve_owner_view(request):
#     return render(request, 'adminApp/approve-owner.html')

def manage_customer_view(request):
    u = Profile.objects.filter(verified=True).exclude(user__profile__userType='Admin').exclude(user=request.user)
    if request.method == "POST":
        search = request.POST.get("search")
        u = Profile.objects.filter(user__first_name__icontains=search, verified=True).exclude(user__profile__userType='Admin').exclude(user=request.user)
        
    page = request.GET.get('page', 1)

    paginator = Paginator(u, 10)
    try:
        u = paginator.page(page)
    except PageNotAnInteger:
        u = paginator.page(1)
    except EmptyPage:
        u = paginator.page(paginator.num_pages)
    return render(request, 'adminApp/manage-customer.html', {'user':u})

    # return render(request, 'adminApp/manage-customer.html')

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
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        photo = request.FILES.get('pic')
        address= request.POST.get('address')
        
        if pass1!=pass2:
            msg= _('Password should be same.')
            return render(request,'adminApp/add-admin.html',{'msg':msg})
        if len(contact)!=10:
            msg= _('Contact should be 10 digit.')
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
            msg= _('Usename already exist.')
            return render(request,'adminApp/add-admin.html',{'msg':msg})
        Profile.objects.create(
            user=user,
            photo=photo,
            contact_No=contact,
            address=address,
            userType="Admin"
            )
        return redirect('/all-user/')
    return render(request, 'adminApp/add-admin.html')




def add_house_owner(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        photo = request.FILES.get('pic')
        address= request.POST.get('address')
        
        if pass1!=pass2:
            msg= _('Password should be same.')
            return render(request,'adminApp/add-house-owner.html',{'msg':msg})
        if len(contact)!=10:
            msg= _('Contact should be 10 digit.')
            return render(request,'adminApp/add-house-owner.html',{'msg':msg})
        try:
            user=User.objects.create_user(
                username=username,
                email=email,
                password=pass1,
                first_name=first_name,
                last_name=last_name
                )
        except:
            msg= _('Usename already exist.')
            return render(request,'adminApp/add-house-owner.html',{'msg':msg})
        Profile.objects.create(
            user=user,
            photo=photo,
            contact_No=contact,
            address=address,
            userType="Owner"
            )
        return redirect('manage-customer')
    return render(request, 'adminApp/add-house-owner.html')
    


def add_tenant(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        photo = request.FILES.get('pic')
        address= request.POST.get('address')
        
        if pass1!=pass2:
            msg= _('Password should be same.')
            return render(request,'adminApp/add-tenant.html',{'msg':msg})
        if len(contact)!=10:
            msg= _('Contact should be 10 digit.')
            return render(request,'adminApp/add-tenant.html',{'msg':msg})
        try:
            user=User.objects.create_user(
                username=username,
                email=email,
                password=pass1,
                first_name=first_name,
                last_name=last_name
                )
        except:
            msg= _('Usename already exist.')
            return render(request,'adminApp/add-tenant.html',{'msg':msg})
        Profile.objects.create(
            user=user,
            photo=photo,
            contact_No=contact,
            address=address,
            userType="Public"
            )
        
        return redirect('manage-customer')
    return render(request, 'adminApp/add-tenant.html')
    



    # if request.method == 'GET':
    #     user_form = UserForm()
    #     profile_form = AdminProfileForm()
    #     location_form = LocationForm()
    
    #     return render(request, 'adminApp/add-admin.html', {'user_form':user_form,'profile_form': profile_form, 'location_form': location_form})
    
    # elif request.method == 'POST':
    #     user_form = UserForm(request.POST)
    #     profile_form = AdminProfileForm(request.POST, request.FILES)
    #     location_form = LocationForm(request.POST)
        
    #     return render(request, 'adminApp/add-admin.html', {'user_form':user_form,'profile_form': profile_form, 'location_form': location_form})



def manage_owner_task(request):
    return render(request, 'adminApp/manage-owner-task.html')


    
    
def add_listing(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'adminApp/add-listing.html', {'form': form , 'profiles':profiles})

    
     
def Approve_listing(request):
    L = Listing.objects.filter(approved=False)
    if request.method == "POST":
        search = request.POST.get("search")
        # seller = seller.user.username
        # seller = request.user.profile 
        L = Listing.objects.filter(user__house_kind__icontains=search, approved=False)
    
    page = request.GET.get('page', 1)

    paginator = Paginator(L, 10)
    try:
        L = paginator.page(page)
    except PageNotAnInteger:
        L = paginator.page(1)
    except EmptyPage:
        L = paginator.page(paginator.num_pages)

    return render(request, 'adminApp/approve-owner.html',  {'listing':L})


def retrieve_images(request, L):
    try:
        listing = Listing.objects.get(id=L)
        images = listing.image.all()  # Retrieve the images related to the listing
        context = {
            'listing': listing,
            'images': images
        }
        return render(request, 'adminApp/listing_images.html', context)
    except Image.DoesNotExist:
        return render(request, 'adminApp/images_not_found.html')
        


def approve_owner_request(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    # Perform logic to approve the owner request, such as updating the verified flag
    listing.approved = True
    listing.save()
    
    subject = 'Listing Approved'
    from_email = settings.EMAIL_HOST_USER
    to_email = ['lema2127@gmail.com']
    
    messages.info(request, 'Welcome To Housing At Wolkite')
    messages.success(request, 'Listing has been verified.')
    
    html_content = render_to_string('adminApp/email_template.html', {'variable1': 'Welcome To Housing At Wolkite', 'variable2': 'Listing has been verified.'})
    # Create the email message
    email_message = EmailMultiAlternatives(subject, body=None, from_email=from_email, to=to_email)
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()
    
    
   
    
    # Redirect to a success page or back to the listing details page
    return redirect('master')





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








        
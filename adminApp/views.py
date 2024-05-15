from django.shortcuts import render,redirect,get_object_or_404
from users.models import Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.conf import settings
from main.models import Listing,Image
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from message.models import Conversation
from paymnet.models import Booking,Payment
from django.contrib.auth.decorators import login_required
from main.models import Upload

def display_all_bookings(request):
    # Fetch all bookings from the database
    bookings = Booking.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(bookings, 10)
    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        bookings = paginator.page(1)
    except EmptyPage:
        bookings = paginator.page(paginator.num_pages)
    
    # Render the template with bookings data
    return render(request, 'adminApp/bookings.html', {'bookings': bookings})



def display_all_payments(request):
    # Fetch all bookings from the database
    # bookings = Booking.objects.all()
    all_payments = Payment.objects.all()
    all_bookings = Booking.objects.all()
    
    
    page = request.GET.get('page', 1)

    paginator = Paginator(all_bookings, 1)
    try:
        all_bookings = paginator.page(page)
    except PageNotAnInteger:
        all_bookings = paginator.page(1)
    except EmptyPage:
        all_bookings = paginator.page(paginator.num_pages)
        
    context = {
        

        'all_payments': all_payments,
        'all_bookings': all_bookings
    }

    
    return render(request, 'adminApp/paymenthistory.html', context) 




def admin_view(request):
    return render(request, 'adminApp/adminHome.html')


    
def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
   

   

    available_house = Listing.objects.filter(approved=True).count()
    booked_house = Booking.objects.filter(booking_status="Confirmed").count()

    customer_request = Upload.objects.filter(status="Pending").count()

    # my_house = House.objects.filter(user=UserProfile.objects.get(user=request.user)).count()
    # my_available_house = House.objects.filter(user=UserProfile.objects.get(user=request.user), status="Available").count()

    # my_booking = BookingRequest.objects.filter(user=UserProfile.objects.get(user=request.user)).count()

    Dict = {
       
    
        "available_house":available_house,
        "booked_house":booked_house,
        "customer_request":customer_request,

    }
    return render(request, 'adminApp/board.html',Dict)



# def approve_owner_view(request):
#     return render(request, 'adminApp/approve-owner.html')




def manage_customer_view(request):
    
    u = Profile.objects.exclude(user__profile__userType='Admin')
    if request.method == "POST":
        search = request.POST.get("search")
        u = Profile.objects.filter(user__first_name__icontains=search, verified=True)
        # exclude(user__profile__userType='Admin')
    page = request.GET.get('page', 1)

    paginator = Paginator(u, 10)
    try:
        u = paginator.page(page)
    except PageNotAnInteger:
        u = paginator.page(1)
    except EmptyPage:
        u = paginator.page(paginator.num_pages)
    return render(request, 'adminApp/manage-users.html', {'user':u})



def ViewUser(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    u = Profile.objects.get(id=id)
    
    return render(request, 'adminApp/view_user.html',{'user':u})




@login_required
def delete_profile(request, user_id):
    # Retrieve the profile object using the provided user ID
    profile = get_object_or_404(Profile, user_id=user_id)
    
    if request.method == 'POST':
        # If the request method is POST, delete the profile
        profile.delete()
        # Redirect to a success page or another appropriate URL
        return redirect('all-user')
    
    # Render a confirmation page for profile deletion
    return render(request, 'adminApp/view_user.html', {'user': profile})



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
        messages.info(request, 'An admin Registered seccessfully')
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
        messages.info(request, 'An house owner Registered seccessfully')
        return redirect('/manage-customer/')
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
        
        messages.info(request, 'A tenant Registered seccessfully')
        return redirect('/manage-customer/')
    return render(request, 'adminApp/add-tenant.html')
    



   


def manage_owner_task(request):
    return render(request, 'adminApp/manage-owner-task.html')

    
     
def Approve_listing(request):
    L = Listing.objects.filter(approved=False)
  
    if request.method == "POST":
        search = request.POST.get("search")
        # seller = seller.user.username
        # seller = request.user.profile 
        L = Listing.objects.filter(house_kind__icontains=search, approved=False)
    
    page = request.GET.get('page', 1)

    paginator = Paginator(L,5)
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
    to_email = ['israelbeyene92@gmail.com']
    
    messages.info(request, 'Listing Accepted')

    
    html_content = render_to_string('adminApp/email_template.html', {'variable1': 'Welcome To Housing At Wolkite', 'variable2': 'Listing has been verified.'})
    # Create the email message
    email_message = EmailMultiAlternatives(subject, body=None, from_email=from_email, to=to_email)
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()
    # Redirect to a success page or back to the listing details page
    return redirect('approve-owner')



def reject_owner_request(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    # Perform logic to approve the owner request, such as updating the verified flag
    listing.approved = False
    listing.save()
    
    subject = 'Listing Rejected'
    from_email = settings.EMAIL_HOST_USER
    to_email = ['israelbeyene92@gmail.com']
    
    messages.info(request, 'Listing Rejected')
  
    
    html_content = render_to_string('adminApp/email_template.html', {'variable1': 'Welcome To Housing At Wolkite', 'variable2': 'Listing has been verified.'})
    # Create the email message
    email_message = EmailMultiAlternatives(subject, body=None, from_email=from_email, to=to_email)
    email_message.attach_alternative(html_content, "text/html")
    email_message.send()
    # Redirect to a success page or back to the listing details page
    return redirect('approve-owner')

from django.contrib.auth import authenticate, login

def ChangePassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    msg = ''
    if request.method == "POST":
        username = request.user.username
        oldpass = request.POST.get('oldpass')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1!=password2:
            msg='New and Confirm Password should be same.'
            return render(request,'adminApp/changepass.html', {'msg':msg})
              
        user = User.objects.get(username=username)
        newpass = user.check_password(oldpass)
        
        if newpass:
            user.set_password(password1)
            user.save()
            data=authenticate(username=username,password=password1)
            if data !=None:
                login(request,data)
                return redirect('profile')
        msg='Old Password should be same.'
    return render(request,'adminApp/changepass.html', {'msg':msg})








def EditProfile(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    u = Profile.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        photo = request.FILES.get('pic')
        contact = request.POST.get('contact')

        if len(contact)!=10:
            msg = "Contact number should be 10 digit"
            return render(request,'adminApp/edit-profile.html', {'details':u, 'msg':msg})
        
        if photo:
            u.photo = photo
 
        u.address = address
        u.contact_No = contact

        u.user.email = email
        u.user.first_name = first_name
        u.user.last_name = last_name
        u.user.save()
        u.save()
        return redirect('profile')
    return render(request,'adminApp/edit-profile.html', {'details':u})





def profile_of_users(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'adminApp/profile.html')



from  users.models import Profile


@login_required
def AllUser(request):
    
    u = Profile.objects.exclude(user=request.user)
    if request.method == "POST":
        search = request.POST.get("search")
        u = Profile.objects.filter(user__first_name__icontains=search, verified=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(u, 7)
    try:
        u = paginator.page(page)
    except PageNotAnInteger:
        u = paginator.page(1)
    except EmptyPage:
        u = paginator.page(paginator.num_pages)
    return render(request, 'adminApp/all-user.html', {'user':u})






def AdminHelpDesk(request):
    u = Profile.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = 'From Home Rental Service'
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        if u.userType == "Admin" or request.user.is_superuser or request.user.is_staff:
            body = f'Hi,  \n \n \t  email: {email} \n \n \t message: {message} \n\n Thanks, \n From Admin, \nHome Rental Service'
        else:
            body = f'Hi {email}, \n \n \t message: {message} \n\n Thanks, \n From Owner, \nHome Rental Service'         
        send_mail(subject, body, from_email, to_email, fail_silently=True)

    return render(request, 'adminApp/admin-helpdesk.html')



def HelpDesk(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        message = request.POST.get('message')
        subject = 'From Home Rental Service'
        body = f'Hi Admin, \n \n \t {request.user.first_name} is trying to contact you. \n \n \t  email: {request.user.email} \n \n \t message: {message} \n\n Thanks, \n Home Rental Service'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['israelbeyene92@gmail.com']
        send_mail(subject, body, from_email, to_email, fail_silently=True)
    return render(request, 'main/owner/helpdesk.html')



def admin_tenant_messaging(request,recipient_username):
    return render(request, 'adminApp/adminMessage.html', {'recipient_username': recipient_username})


def landlord_admin_messaging(request):
    admin = request.user
    conversations = Conversation.objects.filter(members=admin)
    context = {
        'conversations': conversations
    }
    return render(request, 'adminApp/out_box.html', context)

        





def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'adminApp/manage-customer.html', {'bookings': bookings})
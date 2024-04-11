from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from .forms import UserForm,ProfileForm,LocationForm
from main.models import Listing,LikedListing
from .models import Profile,OTP
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from twilio.rest import Client
from django.conf import settings
import random
import string

def LoginPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('home')
            else:
                messages.error(request, f'error occured during tying to login')
        else:
             messages.error(request, f'error occured during tying to login')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'users/login.html', {'login_form': login_form})


def Logout(request):
    logout(request)
    return redirect('login')






def send_verification_code(phone_number, verification_code):
    account_sid = 'AC9e0e9e306fc840441b99c1e42bed7ceb'
    auth_token = 'be97b4af4ba9ee71fba7a86ebf92e66f'
    twilio_phone_number = '+1 470 239 6493'
    client = Client(account_sid, auth_token)
    
     # Send the verification code
    message = client.messages.create(
        body=f"Your verification code is: {verification_code}",
        from_ = twilio_phone_number,
        to=phone_number
    )

    # Return the message SID
    return message.sid
        
        
        
        

def SignPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        # profile_pic = request.FILES.get('pic')
        address= request.POST.get('address')
        
        if pass1!=pass2:
            msg= _('Password should be same.')
            return render(request,'sign.html',{'msg':msg})
        if len(contact)!=10:
            msg= _('Contact should be 10 digit.')
            return render(request,'users/sign.html',{'msg':msg})
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
            return render(request,'users/sign.html',{'msg':msg})
        Profile.objects.create(
            user=user,
            # profilePicture=profile_pic,
            contact_No=contact,
            address=address,
            verified=True
            )
        
        verification_code = generate_verification_code()  # Replace with your code to generate a verification code
        verification_request_id = send_verification_code(contact, verification_code)
        print("Verification request ID:", verification_request_id)
        request.session['verification_code'] = verification_code

        return redirect('verify_phone')
        # return redirect('login')
    return render(request, 'users/sign.html')




def generate_verification_code():
    code_length = 6  # Set the desired length of the verification code
    characters = string.digits  # Use digits for a numeric verification code

    verification_code = ''.join(random.choice(characters) for _ in range(code_length))
    return verification_code

# Assume you have the necessary imports and other code here

def verify_phone(request):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')
        expected_code = request.session.get('verification_code')

        if entered_code == expected_code:
            # Phone number is verified
            # Perform any necessary actions, such as updating the user's verified status
            return redirect('login')  # Redirect to the login page
        else:
            # Verification code does not match
            # Handle the error condition appropriately
            error_message = "Invalid verification code."
            return render(request, 'users/verify_phone.html', {'error_message': error_message})

    return render(request, 'users/verify_phone.html')





def OwnerSign(request):
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
            return render(request,'users/owner-sign.html',{'msg':msg})
        if len(contact)!=10:
            msg= _('Contact should be 10 digit.')
            return render(request,'users/owner-sign.html',{'msg':msg})
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
            return render(request,'users/owner-sign.html',{'msg':msg})
        Profile.objects.create(
            user=user,
            photo=photo,
            contact_No=contact,
            address=address,
            userType="Owner"
            )
        return redirect('/login/')
    return render(request, 'users/owner-sign.html')


def ForgotPage(request):
    return render(request, 'users/forgot.html')    


def SendEmailForForgotPassword(request):
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            msg = 'Invalid Username.'
            return render(request, 'users/forgot.html', {'msg': msg})

        if not user.email:
            msg = 'There is no Email Associated with this Account.'
            return render(request, 'users/forgot.html', {'msg': msg})

        otp = OTP.objects.create(user=user)

        body = f'Did you forget your password? No worries!\n\nThis is your OTP to reset your password: {otp.otp}\n\nThank you!'
        subject = 'Forgot Password for House Rental Account'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject, body, from_email, to_email, fail_silently=False)
        return redirect('forgotpassword')

    return render(request, 'users/forgot.html')
    # return render(request, 'forgot.html')




def ForgotPassword(request):
    msg = ''
    
    if request.method == "POST":
        username = request.POST.get('username')
        user_otp = request.POST.get('otp')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            msg = 'Passwords should be the same.'
            return render(request, 'users/forgotpassword.html', {'msg': msg})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            msg = 'Invalid Username.'
            return render(request, 'users/forgot.html', {'msg': msg})

        otp = OTP.objects.filter(user=user).order_by('-created_at').first()
        if otp and str(otp.otp) == user_otp:
            user.set_password(password1)
            user.save()
            return redirect('login')

        msg = 'Please enter the correct OTP.'
        return redirect('login')

    return render(request, 'users/forgotpassword.html', {'msg': msg})


        
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
        








# def send_verification_code(phone_number, verification_code):
#     client = Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
#     sms = Sms(client)
    
    
#     response = sms.send_message({
#         "from": settings.VONAGE_PHONE_NUMBER,
#         "to": phone_number,
#         "text": f"Your verification code is: {verification_code}"
#     })



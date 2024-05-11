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
from django.utils.translation import gettext as _
# from email_validator import validate_email, EmailNotValidError # type: ignore
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages


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
                return redirect('main:home')
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




        

def SignPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        
        
        phone_number = contact
        country_code = 'ET'
        if not validate_phone_number(phone_number, country_code): 
            messages.error(request, 'Invalid Phone Number')
            return render(request,'users/sign.html')
            # Replace 'US' with the appropriate country code
             
        if not is_strong_password(pass1):
            messages.warning(request, 'Password Must be Strong')
            return render(request,'users/sign.html')
        
        if not is_strong_password(pass2):
            messages.warning(request, 'Password Must be Strong')
            return render(request,'users/sign.html')
        
        if not validate_name(username): 
            messages.warning(request, 'Not Valid Name')
            return render(request,'users/sign.html')
        
        if not validate_name(first_name): 
            messages.warning(request, 'Not Valid Name')
            return render(request,'users/sign.html')
        
        if not validate_name(last_name): 
            messages.warning(request, 'Not Valid Name')
            return render(request,'users/sign.html')
            
        if not validate_email(email):
            messages.warning(request, 'Invalid Email Address')
            return render(request,'users/sign.html')
        
        
        
        
        if pass1 != pass2:
            msg = _('Password should be same.')
            return render(request, 'users/sign.html', {'msg': msg})
        if len(contact) != 10:
            msg = _('Contact should be 10 digits.')
            return render(request, 'users/sign.html', {'msg': msg})

        # try:
        #     email_object = validate_email(email)
        # except EmailNotValidError as e:
        #     messages.warning(request, f'{e}')
        #     return render(request, 'users/sign.html', {'msg': f'{e}'})

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=pass1,
                first_name=first_name,
                last_name=last_name
            )
        except:
            msg = _('Username already exists.')
            return render(request, 'users/sign.html', {'msg': msg})

        Profile.objects.create(
            user=user,
            contact_No=contact,
            address=address,
            verified=False
        )

        messages.success(request, 'You have been successfully Registered')
        return redirect('login')
    return render(request, 'users/sign.html')



    
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def validate_email(email):
    email_validator = EmailValidator()

    try:
        email_validator(email)
    except ValidationError:
        # Email is not valid
        return False

    # Email is valid
    return True



def validate_name(name):
    name_validator = RegexValidator(
        regex=r'^[A-Za-z]+$',
        message='Name should only contain alphabets.'
    )

    try:
        name_validator(name)
    except ValidationError:
        # Name is not valid
        return False

    # Name is valid
    return True



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
        
        phone_number = contact
        country_code = 'ET'
        if not validate_phone_number(phone_number, country_code): 
            messages.warning(request, 'Invalid Phone Number')
            return render(request,'users/owner-sign.html')
            # Replace 'US' with the appropriate country code
            
        if not validate_name(username): 
            messages.warning(request, 'Not Valid Name')
            return render(request,'users/owner-sign.html')
        
        if not validate_name(first_name): 
            messages.warning(request, 'Not Valid Name')
            return render(request,'users/owner-sign.html')
        
        if not validate_name(last_name): 
            messages.warning(request, 'Not Valid Name')
            return render(request,'users/owner-sign.html')
             
        if not is_strong_password(pass1):
            messages.warning(request, 'Password Must be Strong')
            return render(request,'users/owner-sign.html')
        
        if not is_strong_password(pass2):
            messages.warning(request, 'Password Must be Strong')
            return render(request,'users/owner-sign.html')
            
            
        if not validate_email(email):
            messages.warning(request, 'Invalid Email Address')
            return render(request,'users/owner-sign.html')
        
        
        if pass1!=pass2:
            msg= _('Password should be same.')
            return render(request,'users/owner-sign.html',{'msg':msg})
        if len(contact)!=10:
            messages.warning(request, 'Contact should be 10 digit.')
            return render(request,'users/owner-sign.html')
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
        
        # send_activation_email(request, user)
        messages.success(request, 'You have been successfully Registered')
        return redirect('/login/')
    return render(request, 'users/owner-sign.html')


name = 'israel'
is_valid = validate_name(name)
print(is_valid)



import re

def is_strong_password(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()-=_+[\]{}|;:,.<>/?]', password):
        return False

    # All checks passed, password is strong
    return True



import phonenumbers

def validate_phone_number(phone_number, country_code):
    try:
        parsed_number = phonenumbers.parse(phone_number, country_code)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False
    
    


  




def send_activation_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
    token = default_token_generator.make_token(user)

    activation_url = reverse('activate_account', kwargs={'uidb64': uid, 'token': token})
    activation_link = request.build_absolute_uri(activation_url)

    subject = 'Account Verification'
    from_email = 'fikefiresew1234@gmail.com'  # Replace with your email address
    to_email = user.email

    context = {
        'username': user.username,
        'activation_link': activation_link
    }

    text_content = 'Please click the link below to verify your account:'
    html_content = render_to_string('verification_email.html', context)

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()






def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Activate the user's account
        user.is_active = True
        user.save()

        messages.success(request, 'Your account has been activated. You can now log in.')
    else:
        messages.error(request, 'Invalid activation link.')

    return redirect('login')
        




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











# def send_verification_code(phone_number, verification_code):
#     client = Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
#     sms = Sms(client)
    
    
#     response = sms.send_message({
#         "from": settings.VONAGE_PHONE_NUMBER,
#         "to": phone_number,
#         "text": f"Your verification code is: {verification_code}"
#     })



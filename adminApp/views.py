from django.shortcuts import render,redirect
from users.models import Profile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# Create your views here.


def admin_sign_view(request):
    return render(request, 'adminApp/add-admin.html')
    
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
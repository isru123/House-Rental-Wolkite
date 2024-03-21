from django.shortcuts import render

# Create your views here.


def admin_sign_view(request):
    return render(request, 'users/admin-sign.html')
    
from django.urls import path
from .views import LoginPage, Logout, ProfileView, SignPage,OwnerSign,SendEmailForForgotPassword,ForgotPage,ForgotPassword
from main.views import master_view


urlpatterns = [
    path('master/', master_view , name='master'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginPage, name='login'),
    path('sign/', SignPage , name='sign'),
    path('owner-sign/', OwnerSign, name='owner-sign'),
    path('sendotp/', SendEmailForForgotPassword, name='sendotp'),
    path('forgot/',ForgotPage),
    path('forgotpassword/', ForgotPassword  , name='forgotpassword'),
    path('logout/', Logout, name='logout'),
]



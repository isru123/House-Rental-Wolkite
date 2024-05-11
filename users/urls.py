from django.urls import path
from .views import LoginPage, Logout, activate_account,SignPage,OwnerSign,SendEmailForForgotPassword,ForgotPage,ForgotPassword
from main.views import master_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('master/', master_view , name='master'),
    
    path('login/', LoginPage, name='login'),
    path('sign/', SignPage , name='sign'),
    path('owner-sign/', OwnerSign, name='owner-sign'),
    path('sendotp/', SendEmailForForgotPassword, name='sendotp'),
    path('forgot/',ForgotPage),
    path('forgotpassword/', ForgotPassword  , name='forgotpassword'),
    path('logout/', Logout, name='logout'),

    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate_account'),

    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]



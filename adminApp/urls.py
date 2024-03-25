
from django.urls import path
from main.views import master_view
from .views import admin_sign_view,AllUser



urlpatterns = [
    path('master/', master_view , name='master'),
    path('admin-sign/', admin_sign_view , name='admin-sign'),
    path('all-user/', AllUser, name='all-user'),
]



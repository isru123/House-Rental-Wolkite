
from django.urls import path
from main.views import master_view
from .views import admin_view,AllUser



urlpatterns = [
    path('master/', master_view , name='master'),
    path('admin_home/', admin_view, name='admin_home'),
    path('all-user/', AllUser, name='all-user'),
]




from django.urls import path
from main.views import master_view
from .views import admin_view,AllUser,dashboard_view,approve_owner_view 



urlpatterns = [
    path('master/', master_view , name='master'),
    path('admin_home/', admin_view, name='admin_home'),
    path('all-user/', AllUser, name='all-user'),
    path('dashboard/', dashboard_view, name='dashboard2'),
    path('approve-owner/', approve_owner_view , name='approve-owner' ),
]




from django.urls import path
from main.views import master_view
from .views import admin_view,AllUser,Dashboard,approve_owner_view ,add_admin_view,manage_customer_view,ViewUser,DeleteUser



urlpatterns = [
    path('master/', master_view , name='master'),
    path('admin_home/', admin_view, name='admin_home'),
    path('all-user/', AllUser, name='all-user'),
    path('dashboard/', Dashboard, name='board'),
    path('approve-owner/', approve_owner_view , name='approve-owner' ),
    path('add-admin/', add_admin_view , name='add-admin'),
    path('manage-customer/', manage_customer_view , name='manage-customer'),
    path('view-user/<int:id>/', ViewUser , name='view_user'),
    path('delete-user/<int:id>/', DeleteUser, name='delete_user'),
]


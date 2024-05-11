
from django.urls import path
from main.views import master_view
from .views import admin_view,AllUser,Dashboard ,add_admin_view,manage_customer_view,ViewUser,DeleteUser,Approve_listing,retrieve_images,approve_owner_request,manage_owner_task
from .views import reject_owner_request,Profile,EditProfile,ChangePassword,add_listing,add_house_owner,add_tenant,AdminHelpDesk,HelpDesk,admin_tenant_messaging,landlord_admin_messaging


urlpatterns = [
    path('master/', master_view , name='master'),
    path('admin_home/', admin_view, name='admin_home'),
    path('all-user/', AllUser, name='all-user'),
    path('dashboard/', Dashboard, name='board'),
    # path('approve-owner/', approve_owner_view , name='approve-owner' ),
    path('add-admin/', add_admin_view , name='add-admin'),
    path('manage-customer/', manage_customer_view , name='manage-customer'),
    path('view-user/<int:id>/', ViewUser , name='view_user'),
    path('delete-user/<int:id>/', DeleteUser, name='delete_user'),
    path('approve-owner/', Approve_listing , name='approve-owner'),
    path('retrieve-images/<uuid:L>/', retrieve_images, name='retrieve_images'),
    path('approve-owner-request/<uuid:listing_id>/', approve_owner_request, name='approve_owner_request'),
    path('reject-owner-request/<uuid:listing_id>/', reject_owner_request, name='reject_owner_request'),
    path('manage-owner-task/', manage_owner_task, name='manage-owner-task'),
    path('add-listing/', add_listing , name='add-listing'),
    path('add-house-owner/', add_house_owner, name='add-house-owner'),
    path('add-tenant/', add_tenant , name='add-tenant'),
    path('admin-helpdesk/', AdminHelpDesk, name='admin-helpdesk'),
    path('helpdesk/', HelpDesk , name='helpdesk'),
    path('admin-tenant/<str:recipient_username>/', admin_tenant_messaging, name='admin_tenant'),
    path('landlord-admin/', landlord_admin_messaging, name='landlord_admin'),
    # path('chat/<str:recipient_username>/', views.chat_view, name='chat'),
    path('change-password/', ChangePassword, name='change-password'),
    path('edit-profile/<int:id>/', EditProfile, name='edit-profile'),
    path('profile/',Profile,name='profile'),
]


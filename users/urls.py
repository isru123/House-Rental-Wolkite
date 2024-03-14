from django.urls import path
from .views import login_view, logout_view, ProfileView, RegisterView
from main.views import master_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('master/', master_view , name='master'),
    path('register/', RegisterView.as_view() , name='register'),
    path('logout/', logout_view, name='logout'),  
    path('profile/', ProfileView.as_view(), name='profile'),
]



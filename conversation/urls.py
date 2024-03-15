
from django.urls import path
from main.views import master_view
from .views import message_view



urlpatterns = [
    path('master/', master_view , name='master'),
    path('message/', message_view , name='message'),
]



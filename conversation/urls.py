
from django.urls import path
from main.views import master_view
from .views import message_view,user_contact,chat_message,MessageHistoryListView



urlpatterns = [
    path('master/', master_view , name='master'),
    path('message/', message_view , name='message'),
    path('user-contact', user_contact, name='user-contact'),
    path('chat', chat_message, name='chat'),
    path('history/<int:pk>', MessageHistoryListView.as_view(), name='chat-history'),
]




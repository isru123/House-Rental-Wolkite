from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns

    path('inbox/<uuid:conversation_id>/', views.inbox, name='inbox-view'),
    path('<int:conversation_id>/', views.detail, name='detail'),
    path('new/<uuid:id>/', views.new_conversation, name='new'),
    path('edit-message/<int:message_id>/', views.edit_message, name='edit_message'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
]

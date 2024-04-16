from django.urls import path

from .views import inbox_view,detail,new_conversation,edit_message,delete_message,booking_request_view

urlpatterns = [
    # Other URL patterns
    path('inbox/', inbox_view, name='inbox_view'),
    path('<int:conversation_id>/', detail, name='detail'),
    path('new/<uuid:product_id>/', new_conversation, name='new'),
    path('edit-message/<int:message_id>/',edit_message, name='edit_message'),
    path('delete-message/<int:message_id>/',delete_message, name='delete_message'),
    path('book_request/' , booking_request_view , name="book_request"),
]
# edit_listing/<str:id>/

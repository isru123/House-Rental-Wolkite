from django.urls import path

from .views import inbox_view,booking_ask,detail,new_conversation,edit_message,delete_message,dashboard_view,messages, listigs, books, payments


app_name = 'message'

urlpatterns = [
    # Other URL patterns
    path('inbox/', inbox_view, name='inbox_view'),
    path('<int:conversation_id>/', detail, name='detail'),
    path('new/<uuid:product_id>/', new_conversation, name='new'),
    path('edit-message/<int:message_id>/',edit_message, name='edit_message'),
    path('delete-message/<int:message_id>/',delete_message, name='delete_message'),
    path('dashboard_renter/', dashboard_view, name='dashboard_renter'),
    path('messages/', messages, name='messages'),
    path('listigs/', listigs, name='listigs'),
    path('payments/', payments, name='payments'),
    path('ask/', booking_ask, name="ask"),
    path('books/', books, name='books'),
    


]


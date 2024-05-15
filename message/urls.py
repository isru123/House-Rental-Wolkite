from django.urls import path

<<<<<<< HEAD
from .views import inbox_view,detail,new_conversation,edit_message,delete_message,dashboard_view,messages, listigs, books, payments,update_seen
=======
from .views import inbox_view,booking_ask,detail,new_conversation,edit_message,delete_message,dashboard_view,messages, listigs, books, payments


app_name = 'message'
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

urlpatterns = [
    # Other URL patterns
    path('inbox/', inbox_view, name='inbox_view'),
    path('<int:conversation_id>/', detail, name='detail'),
    path('new/<uuid:product_id>/', new_conversation, name='new'),
    path('edit-message/<int:message_id>/',edit_message, name='edit_message'),
    path('delete-message/<int:message_id>/',delete_message, name='delete_message'),
<<<<<<< HEAD
         path('dashboard_renter/', dashboard_view, name='dashboard_renter'),
                  path('messages/', messages, name='messages'),
                  path('listigs/', listigs, name='listigs'),
                path('payments/', payments, name='payments'),

                  path('books/', books, name='books'),

    path('update_seen/<int:conversation_id>/', update_seen, name='update_seen'),
=======
    path('dashboard_renter/', dashboard_view, name='dashboard_renter'),
    path('messages/', messages, name='messages'),
    path('listigs/', listigs, name='listigs'),
    path('payments/', payments, name='payments'),
    path('ask/', booking_ask, name="ask"),
    path('books/', books, name='books'),
    
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9


]


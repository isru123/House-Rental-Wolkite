from django.urls import path

from .views import inbox_view,detail,new_conversation,edit_message,delete_message,dashboard_view,messages, listigs, books, payments,update_seen

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

                  path('books/', books, name='books'),

    path('update_seen/<int:conversation_id>/', update_seen, name='update_seen'),


]
# edit_listing/<str:id>/

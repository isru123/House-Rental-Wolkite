from django.urls import path

from . import views


urlpatterns = [
    # Other URL patterns
path('inbox/<uuid:conversation_id>/', views.inbox, name='inbox-view'),
    path('<int:conversation_id>/', views.detail, name='detail'),
    path('new/<uuid:product_id>/', views.new_conversation, name='new'),
]
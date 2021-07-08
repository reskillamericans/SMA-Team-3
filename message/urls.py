from django.conf.urls import url
from django.urls import path

from . import views
from .views import MessageThreadList, CreateMessage, CreateMessageThread, MessageThreadView

app_name = 'message'
urlpatterns = [
    path('', MessageThreadList.as_view(), name = 'inbox'),
    path('new-message-thread/', CreateMessageThread.as_view(), name = 'create-message-thread'),
    path('message-thread/<int:pk>/', MessageThreadView.as_view(), name = 'message-thread'),
    path('message/<int:pk>/', CreateMessage.as_view(), name = 'message'),
    path('delete/message-thread/<int:pk>', views.delete_message_thread, name = 'delete-message-thread'),
] 
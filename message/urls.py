from django.conf.urls import url
from django.urls import path

from . import views
from .views import MessageThreadList, CreateMessage, CreateMessageThread, MessageThreadView

app_name = 'message'
url_pattern = [
    path('', MessageThreadList.as_view(), name = 'inbox'),
    path('new-thread/', CreateMessageThread.as_view(), name = 'create-message-thread'),
    path('view-thread/<int:pk>/', MessageThreadView.as_view(), name = 'message-thread'),
    path('message/<int:pk>/', CreateMessage.as_view(), name = 'message'),
    path('message-thread/delete/<int:pk>', views.delete_message_thread, name = 'delete-message-thread')
] 
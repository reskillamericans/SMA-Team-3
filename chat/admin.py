from django.contrib import admin
from chat.models import Message, MessageThread
admin.site.register(Message)
admin.site.register(MessageThread)
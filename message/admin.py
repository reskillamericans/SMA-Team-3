from django.contrib import admin
from .models import Message, MessageThread

# Register your models here.

admin.site.register(Message)
admin.site.register(MessageThread)
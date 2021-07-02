from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import authentication.models as a

# Create your models here.

class MessageThread(models.Model):
    sender = models.ForeignKey(a.User, on_delete = models.CASCADE, related_name = '+')
    receiver = models.ForeignKey(a.User, on_delete = models.CASCADE, related_name = '+')
    unread_message = models.BooleanField(default = False)


class Message(models.Model):
    sender_id = models.ForeignKey(a.User, on_delete = models.CASCADE, related_name ='+')
    receiver_id = models.ForeignKey(a.User, on_delete = models.CASCADE, related_name ='+')
    message_thread = models.ForeignKey('MessageThread', related_name = '+', on_delete = models.CASCADE, blank = True, null = True)
    message = models.CharField(max_length = 500)
    created_at = models.DateTimeField(default = timezone.now)
    read_at = models.DateTimeField(default = timezone.now)
    read_message = models.BooleanField(default = False)

    def __str__(self):
        if self.read_message == True:
            return self.read_at
        return self.read_message

    

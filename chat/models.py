from django.contrib.auth.models import User
from django.db import models
import authentication.models as a


class Message(models.Model):
    sender = models.ForeignKey(a.User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(a.User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    message_thread = models.ForeignKey('MessageThread', related_name='+', on_delete=models.CASCADE, null=True,
                                       blank=True, default=None)
    image = models.ImageField(blank=True, null=True, upload_to='messages/')
    read_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('created_at',)


class MessageThread(models.Model):
    sender = models.ForeignKey(a.User, on_delete=models.CASCADE, related_name='send')
    receiver = models.ForeignKey(a.User, on_delete=models.CASCADE, related_name='receive')
    unread_message = models.BooleanField(null=True, blank=True, default=False)

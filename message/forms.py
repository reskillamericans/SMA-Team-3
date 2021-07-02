from django import forms
from .models import MessageThread, Message

class MessageThreadForm(forms.Form):
    user_id = forms.CharField(label = ' ', max_length = 150)


class MessageForm(forms.Form):
    messages = forms.CharField(label = " ", max_length = 500)
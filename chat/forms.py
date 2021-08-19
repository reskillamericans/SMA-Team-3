from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Message
        fields = ['receiver', 'message', 'image']

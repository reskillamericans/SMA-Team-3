from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import MessageThread, Message

User = get_user_model()

@login_required(login_url='/accounts/login/')
def message_list_details(request):
    messages = Message.objects.filter(Q(sender_id=request.user.id) | Q(receiver_id=request.user.id))
    context = {
        'chats': messages
    }
    return render(request, 'chat/inbox.html', context)

@login_required(login_url='/accounts/login/')
def create_message(request):
    sender = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        username = request.GET.get('username')
        #        receiver = User.objects.get(username=username)

        if username is None or username == '':
            return redirect('posts:home')
        context = {
            'receiver': username
        }
        return render(request, 'chat/create_message.html', context)

    if request.method == 'POST':
        sender = User.objects.get(id=request.user.id)
        message = request.POST.get('message')
        username = request.POST.get('receiver')
        image = request.FILES.get('image')

        if username == '' or message == '':
            return redirect('chat:create-message')

        try:
            receiver = User.objects.get(username=username)
            if sender.username != receiver.username:
                image = image
                new_message = Message(sender=sender, receiver=receiver,
                                      message=message, image=image)
                new_message.save()
                messages.success(request, 'Message Sent!')
                return redirect('posts:home')
            messages.error(request, 'Message cant be sent to self!')
            return redirect('posts:home')

        except User.DoesNotExist:
            messages.error('Cannot find user!')


def message_view(request, pk):
    message = Message.objects.order_by('-created_at').get(pk=pk)
    if message.read_at is None:
        message.read_at = datetime.datetime.now()
        message.save()

    context = {
        'message': message,
    }
    return render(request, 'chat/message_thread.html', context)


def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.receiver == request.user:
        message.delete()
        return redirect('chat:inbox')
    return redirect('chat:inbox')

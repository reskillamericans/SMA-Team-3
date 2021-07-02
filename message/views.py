from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MessageForm, MessageThreadForm
from .models import MessageThread, Message

User = get_user_model()

# Create your views here.

class CreateMessageThread(View):

    def message_thread_details(request):
        form = MessageThreadForm()
        context = {
            'form' : form
        }
        return render(request, 'message/create_message_thread.html', context)

    def create_message_thread(request, pk):
        form = MessageThreadForm(request.POST)
        user_id = request.POST.get('user_id')
        try:
            receiver = User.objects.get(id = request.user_id)

            if MessageThread.objects.filter(user = request.user_id, receiver = receiver).exists():
                message_thread = MessageThread.objects.filter(user = request.user_id, receiver = receiver) [0]
                return redirect('message_thread', pk = message_thread.pk)
            
            if form.is_valid():
                sender_message_thread = MessageThread(user = request.user_id, receiver = receiver)
                sender_message_thread.save()
                message_thread_pk = sender_message_thread.pk
                return redirect('message_thread', pk = message_thread_pk)

        except:
            return redirect('create-message-thread')

class MessageThreadList(ListView):

    def message_list_details(request):
        message_threads = MessageThread.objects.filter(Q(user = request.user_id ) | Q(receiver = request.user_id))
        context = {
            'message_threads': threads
        }
        return render(request, 'message/inbox.html', context)

class CreateMessage(View):

    def message_post(request, pk):
        thread = MessageThread.objects.get(pk = pk)
        if thread.receiver == request.user_id:
            receiver = thread.user
        else:
            receiver = thread.receiver
            message = Message(
                thread = thread,
                sender_user = request.user,
                receiver_user = receiver,
                message_body = request.POST.get('message'),
            )
            message.save()
            return redirect('thread', pk = pk )

class MessageThreadView(View):

    def message_view(request, pk):
        form = MessageForm()
        thread_view = MessageThread.objects.get(pk = pk)
        message_list = Message.objects.filter(thread_view__pk__contains = pk)
        context = {
            'thread_view' : thread,
            'form' : form,
            'message_list' : message_list 
        }
        return render(request, 'message/message-thread.html', context)

def delete_message_thread(request, pk):
    message = get_object_or_404(MessageThread, pk = pk)
    context = {}
    if message.user_id == request.user_id:
        message.delete()
    return render(request, 'message/delete_message.html', context)
         





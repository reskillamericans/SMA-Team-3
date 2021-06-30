from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
import json

from .forms import NewPostForm, UpdatePostForm
from .models import Posts, PostLikes, 

User = get_user_model()


class PostListView(ListView):
    model = Posts
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            liked = [i for i in Posts.objects.all() if PostLikes.objects.filter(liker_id=self.request.user, post_id=i)]
            context['liked_post'] = liked
        return context


@login_required
def create_post(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_name = user
            data.user_id = user
            data.save()
            messages.success(request, f'Posted Successfully')
            return redirect('posts:home')
    else:
        form = NewPostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def update_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST":
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, f'Post Saved Successfully')
            post = data
            return redirect('posts:home')
    form = UpdatePostForm(
        initial={
            'content': post.content,
            'image': post.image,
            'category': post.category,
        }
    )
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    context = {'post': post}
    if request.method == "POST":
        post.delete()
        return redirect('posts:home')
    return render(request, 'posts/delete_post.html', context)


# class AddLike(login_required):
#     def post(self, request, pk, *args, **kwargs):
#         post = Posts.objects.get(pk=pk)
#         is_dislike = False
#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 return request.user
#         if is_dislike:
#             post.dislikes.remove(request.user)
#         is_like = False
#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 return request.user
#         if not is_like: 
#             post.likes.add(request.user)
        
#         if is_like:
#             post.likes.remove(request.user)


# class AddDislike(login_required):
#     def post(self, request, pk, *args, **kwargs):
#         post = Posts.objects.get(pk=pk)
#         is_like = False
#         for like in post.likes.all():
#             if like == request.user:
#                 is_like = True
#                 return request.user
#         if is_like:
#             post.likes.remove(request.user)
#         is_dislike = False
#         for dislike in post.dislikes.all():
#             if dislike == request.user:
#                 is_dislike = True
#                 return request.user
#         if not is_dislike: 
#             post.dislikes.add(request.user)
        
#         if is_dislike:
#             post.dislikes.remove(request.user)
def like_button(request):
   if request.method =="POST":
       if request.POST.get("operation") == "like_submit" and request.is_ajax():
         content_id=request.POST.get("content_id",None)
         content=get_object_or_404(PostLikes,pk=content_id)
         if content.likes.filter(id=request.user.id): #already liked the content
            content.likes.remove(request.user) #remove user from likes 
            liked=False
         else:
             content.likes.add(request.user) 
             liked=True
         ctx={"likes_count":content.total_likes,"liked":liked,"content_id":content_id}
         return HttpResponse(json.dumps(ctx), content_type='application/json')

   contents=PostLikes.objects.all()
   already_liked=[]
   id=request.user.id
   for content in contents:
       if(content.likes.filter(id=id).exists()):
        already_liked.append(content.id)
   ctx={"contents":contents,"already_liked":already_liked}
   return render(request,"like/like_template.html",ctx)

    
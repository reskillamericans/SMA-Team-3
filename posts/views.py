import json

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from authentication.models import UserSocials

from .forms import NewPostForm, UpdatePostForm, NewCommentForm
from .models import Posts, PostLikes, PostComments

User = get_user_model()

@login_required(login_url='/accounts/login/')
def posts_feed(request):
    posts = Posts.objects.order_by('-created_at').all()
    liked = [i for i in Posts.objects.all() if PostLikes.objects.filter(liker_id=request.user, post_id=i)]
    form = NewPostForm()
#    if request.method == 'POST':
#       create_post(request)
    context = {
        'form': form,
        'posts': posts,
        'liked_post': liked
    }
    return render(request, 'posts/home.html', context)


@login_required(login_url='/accounts/login/')
def users_profile(request):
    user = User.objects.get(id=request.user.id)
    post = Posts.objects.filter(user_id=user)
    context = {
        'posts': post
    }
    return render(request, 'posts/user_post.html', context)


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    print(post.image)
    user = User.objects.get(id=request.user.id)
    comment = PostComments.id
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post_id = post
            data.username = user
            data.user_id = user
            data.save()
            if post.id == user.id:
                return redirect('posts:my-profile')
            else:
                return redirect('posts:home')
    else:
        form = NewCommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'form': form, 'comment': comment})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def post_delete(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    context = {'post': post}
    if request.method == "POST":
        post.delete()
        return redirect('posts:home')
    return render(request, 'posts/delete_post.html', context)


@login_required(login_url='/accounts/login/')
def delete_comment(request, pk):
    comment = get_object_or_404(PostComments, pk=pk)
    context = {}
    if comment.user_id == request.user:
        comment.delete()
        return redirect('posts:home')
    return render(request, 'posts/delete_post.html', context)


@login_required(login_url='/accounts/login/')
def like(request, pk):
    user = User.objects.get(id=request.user.id)
    post = get_object_or_404(Posts, pk=pk)
    liked = False
    like = PostLikes.objects.filter(liker_id=user, post_id=post)
    if like:
        like.delete()
    else:
        liked = True
        PostLikes.objects.create(liker_id=user, post_id=post)
    resp = {
        'liked': liked
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")

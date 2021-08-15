from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.posts_feed, name='home'),
    path('user', views.users_profile, name='my-profile'),
    path('like/<int:pk>', views.like, name='post-like'),
    path('new', views.create_post, name='create-post'),
    path('<pk>/update', views.update_post, name='update-post'),
    path('update/<int:pk>', views.update_post, name='update-post'),
    path('delete/<int:pk>', views.post_delete, name='delete'),
    path('comment/<int:pk>', views.post_detail, name='comment'),
    path('<int:pk>', views.post_detail, name='view-post'),
    path('comment/delete/<int:pk>', views.delete_comment, name='delete-comment'),

] 

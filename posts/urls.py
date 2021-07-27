from django.conf.urls import url
from django.urls import path

from . import views
from .views import PostListView

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/', views.users_profile, name='my-profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('new/', views.create_post, name='create-post'),
    path('<pk>/update', views.update_post, name='update-post'),
    path('update/<int:pk>', views.update_post, name='update-post'),
    path('delete/<int:pk>', views.post_delete, name='delete'),
    path('comment/<int:pk>', views.post_detail, name='comment'),
    path('comment/delete/<int:pk>', views.delete_comment, name='delete-comment'),

]

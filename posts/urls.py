from django.conf.urls import url
from django.urls import path

from . import views
from .views import PostListView

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('new/', views.create_post, name='create-post'),
    path('<pk>/update', views.update_post, name='update-post'),
    path('delete/<int:pk>', views.post_delete, name='delete'),

]

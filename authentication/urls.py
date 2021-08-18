from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('users/', views.users_list, name='users_list'),
	path('users/<str:username>/', views.profile_view, name='profile_view'),
	path('friends/', views.friend_list, name='friend_list'),
	path('users/friend-request/send/<int:id>/', views.send_friend_request, name='send_friend_request'),
	path('users/friend-request/cancel/<int:id>/', views.cancel_friend_request, name='cancel_friend_request'),
	path('users/friend-request/accept/<int:id>/', views.accept_friend_request, name='accept_friend_request'),
	path('users/friend-request/delete/<int:id>/', views.delete_friend_request, name='delete_friend_request'),
	path('users/friend/delete/<int:id>/', views.delete_friend, name='delete_friend'),

]

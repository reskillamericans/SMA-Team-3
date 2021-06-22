from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),

]

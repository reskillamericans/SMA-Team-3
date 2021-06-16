from django.urls import path

from . import views

app_name = 'user_accounts'
urlpatterns = [
    path('signup/', views.register, name='register'),

]

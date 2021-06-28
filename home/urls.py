from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('dummy-social', views.home, name='dummy-social'),
]

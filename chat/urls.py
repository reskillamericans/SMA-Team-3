from django.urls import path

from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.message_list_details, name='inbox'),
    path('new-message/<int:id>', views.create_message, name='create-message'),
    path('<int:pk>', views.message_view, name='view-message'),
    path('delete/message/<int:pk>', views.delete_message, name='delete-message'),
]

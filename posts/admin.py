from django.contrib import admin
from .models import Posts, PostCategory, PostLikes, PostComments

# Register your models here.

admin.site.register(Posts)
admin.site.register(PostCategory)
admin.site.register(PostLikes)
admin.site.register(PostComments)

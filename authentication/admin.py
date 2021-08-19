from django.contrib import admin
from .models import User, UserSocials, Followers
# Register your models here.

admin.site.register(User)
admin.site.register(UserSocials)
admin.site.register(Followers)

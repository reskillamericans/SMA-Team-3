from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("Username"), unique=True, max_length=255, null=True, blank=True)
    first_name = models.CharField(_('First Name'), max_length=255, default='user')
    last_name = models.CharField(_('Last Name'), max_length=255, default='user')
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True, default='e@email.com')
    avatar = models.ImageField(blank=True, null=True)
    user_type = models.CharField(max_length=50, default='user')
    status = models.CharField(max_length=50, default='Active')
    verified = models.BooleanField(default=False, blank=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    followers_count = models.IntegerField(default=0, editable=False)
    follows_count = models.IntegerField(default=0, editable=False)
    time_zone = models.CharField(max_length=5, default='EST')
    updated_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)
    created_at = models.TimeField(auto_now_add=True, null=True, blank=True, editable=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserSocials(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    stackoverflow = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.user_id)

class Followers(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    follower_id = models.ManyToManyField(User, related_name='follower_id')
    updated_at =   models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)
    created_at =   models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.user.username)

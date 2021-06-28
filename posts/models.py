from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse

import authentication.models as a


class PostCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)
    created_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)

    def __str__(self):
        if self.name is None:
            return 'Post name is empty'
        return self.name


class Posts(models.Model):
    user_id = models.ForeignKey(a.User, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='posts/static/')
    status = models.CharField(max_length=255, blank=True, null=True)
    like_count = models.IntegerField(default=0, editable=False)
    comment_count = models.IntegerField(default=0, editable=False)
    updated_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)
    created_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.user_id)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostComments(models.Model):
    user_id = models.ForeignKey(a.User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    updated_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)
    created_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)


class PostLikes(models.Model):
    liker_id = models.ForeignKey(a.User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True, null=True, blank=True, editable=False)
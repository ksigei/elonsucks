from django.db import models
from django.contrib.auth.models import User
import uuid

class ForumPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    pictures = models.ManyToManyField('ForumPicture', related_name='forum_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Forum Post'
        verbose_name_plural = 'Forum Posts'

class ForumPicture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to='forum_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

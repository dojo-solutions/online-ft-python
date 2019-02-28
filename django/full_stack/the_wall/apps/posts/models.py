from django.db import models
from ..users.models import User

# Create your models here.
class PostManager(models.Manager):
    pass

class Post(models.Model):
    creator = models.ForeignKey(User, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
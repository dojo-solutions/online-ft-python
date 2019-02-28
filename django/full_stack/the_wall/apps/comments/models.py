from django.db import models
from ..posts.models import Post
from ..users.models import User

# Create your models here.
class CommentManager(models.Manager):
    pass

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments")
    creator = models.ForeignKey(User, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models
from ..users.models import User
from ..posts.models import Post
# Create your models here.
class CommentManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['content']) < 1:
            errors.append("Comment cannot be left blank")

        return errors

    def easy_create(self, form, user_id):
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=form['post_id'])
        Comment.objects.create(
            content=form['content'],
            creator=user,
            post=post
        )

class Comment(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name="created_comments")
    post = models.ForeignKey(Post, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

    def __repr__(self):
        return f"<Comment id:{self.id}>"

    def __str__(self):
        return f"<Comment id:{self.id}>"
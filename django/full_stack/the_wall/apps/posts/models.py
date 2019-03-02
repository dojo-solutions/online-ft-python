from django.db import models
from ..users.models import User

# Create your models here.
class PostManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['content']) < 1:
            errors.append("Post cannot be left empty")

        return errors

    def easy_create(self, form, user_id):
        user = User.objects.get(id=user_id)
        Post.objects.create(
            content=form['content'],
            creator=user
        )

    def easy_delete(self, post_id, user_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.creator.id != user_id:
                return
            post.delete()
        except:
            print("POST DOESNT EXIST")

class Post(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, related_name="created_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

    def __repr__(self):
        return f"<Post id:{self.id}>"

    def __str__(self):
        return f"<Post id:{self.id}>"
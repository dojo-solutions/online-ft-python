from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form):
        errors = []

        if len(form['first_name']) < 2:
            errors.append("First name must be greater than 2 characters long.")

        if len(form['last_name']) < 2:
            errors.append("Last name must be greater than 2 characters long.")

        if not EMAIL_REGEX.match(form['email']):
            errors.append("Email must be valid.")

        existing_users = User.objects.filter(email=form['email'])
        if existing_users:
            errors.append("Email already in use.")

        if len(form['password']) < 8:
            errors.append("Password must be greater than 8 characters long.")

        return errors
    
    def easy_create(self, form):
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            pw_hash = pw_hash,
        )
        return user.id

    def login(self, form):
        existing_users = User.objects.filter(email=form['email'])
        if existing_users:
            user = existing_users[0]
            if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                return (True, user.id)
        return (False, "Email or password incorrect.")

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User: {self.email}>"

    def __str__(self):
        return f"<User: {self.email}>"
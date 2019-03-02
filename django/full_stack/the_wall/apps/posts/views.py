from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

# Create your views here.
def create(req):
    errors = Post.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
    else:
        #create a post
        Post.objects.easy_create(req.POST, req.session['user_id'])
    return redirect('/')

def destroy(req, post_id):
    Post.objects.easy_delete(post_id, req.session['user_id'])
    return redirect('/')
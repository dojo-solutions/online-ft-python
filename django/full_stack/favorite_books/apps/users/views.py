from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def new(req):
    return render(req, 'users/new.html')

def create(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:new')
    # create user
    user_id = User.objects.easy_create(req.POST)
    req.session['user_id'] = user_id
    return redirect('dashboard:index')

def login(req):
    valid, response = User.objects.login(req.POST)
    if not valid:
        messages.error(req, response)
        return redirect('users:new')
    
    req.session['user_id'] = response
    return redirect('dashboard:index')

def logout(req):
    req.session.clear()
    return redirect('users:new')
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
    return render(req, 'users/index.html')

def success(req):
    if 'user_id' not in req.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id=req.session['user_id'])
    }
    return render(req, 'users/success.html', context)

def create(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('/')
    # create user
    user_id = User.objects.easy_create(req.POST)
    req.session['user_id'] = user_id
    return redirect('/success')

def login(req):
    valid, response = User.objects.login(req.POST)
    if not valid:
        messages.error(req, response)
        return redirect('/')
    
    req.session['user_id'] = response
    return redirect('/success')

def logout(req):
    req.session.clear()
    return redirect('/')
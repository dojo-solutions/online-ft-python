from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(req):
    if 'count' not in req.session:
        req.session['count'] = 0
    req.session['count'] += 1

    req.session['random_word'] = get_random_string(length=14)
    return render(req, 'main/index.html')

def generate(req):
    return redirect('/')

def reset(req):
    req.session.clear()
    return redirect('/')
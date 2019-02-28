from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(req):
    if 'user_id' not in req.session:
        return redirect('users:new')
    return HttpResponse("success")
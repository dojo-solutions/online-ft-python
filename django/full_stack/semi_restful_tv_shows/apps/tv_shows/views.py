from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(req):
    return render(req, 'tv_shows/index.html')

def process(req):
    date = datetime.strptime(req.POST['date'], "%Y-%m-%d")
    print(date)
    now = datetime.now()
    print(now.date())
    if now < date:
        print("Date is in the future")
    else:
        print("Date is in the past")
    return redirect('/')
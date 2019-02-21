from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(req):
    context = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M %p")
    }
    return render(req, 'main/index.html', context)
from django.shortcuts import render
from ..users.models import User
from ..posts.models import Post

# Create your views here.
def index(req):
    if 'user_id' not in req.session:
        return redirect('/users/new')
    
    context = {
        'user': User.objects.get(id=req.session['user_id']),
        'posts': Post.objects.all().order_by("-created_at")
    }

    return render(req, 'dashboard/index.html', context)

def wall(req):
    pass
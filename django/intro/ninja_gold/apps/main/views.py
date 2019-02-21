from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    return render(req, 'main/index.html')

def process_money(req, location):
    location_map = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }

    curr_gold = location_map[location]
    time = datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
    activity = {}
    if curr_gold > 0:
        activity['content'] = f"Earned {curr_gold} gold from the {location}! ({time})"
        activity['css_color'] = "green"
    else:
        activity['content'] = f"Entered a {location} and lost {curr_gold} golds... Ouch.. ({time})"
        activity['css_color'] = "red"
    
    req.session['gold'] += curr_gold
    
    if 'activities' not in req.session:
        req.session['activities'] = []
    req.session['activities'].insert(0, activity)
    # this is necessary in django if we're adding something to a nested list or dictionary
    req.session.modified = True
    return redirect('/')
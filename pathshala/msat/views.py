from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import MSAT
from django.contrib.auth import authenticate,get_user
import datetime
from .questions import *

@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        context = {}
        User = get_user(request) 
        if request.method == 'POST':
            #print(request.POST)
            obj = MSAT(
                #r_id = request.POST['r_id'],
                #stud_id = request.user.get_username(),
                response = request.POST['response'],
                timestamp = request.POST['timestamp'],
                mark_scored = request.POST['mark_scored'],
                answered = request.POST['answered'],
                #email = request.session['email']
            )
            obj.save()
        else:
            
            a = User.Class  
            """
            a = request.session['Class']"""
            if a == 8:
                context["class"]=questions_8
            elif a == 9:
                context["class"]=questions_9
            elif a == 10:
                context["class"]=questions_10
            elif a == 11:
                context["class"]=questions_11
            else:
                context["class"]=questions_12
            
            # context["class"]=request.GET['std']
        return render(request,'templates/msat/home.html',context)
    else:
        return redirect('signup')


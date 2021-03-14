from django.shortcuts import render
from django.contrib.auth import authenticate, get_user
from django.utils.safestring import mark_safe
import json
from chatapp.models import Room,Message
from chatapp.forms import RoomForm
import pyrebase

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)#, request.FILES or None)
        print(form.errors)
        if form.is_valid():
            form.save()
    else:
        form = RoomForm()

    return render(request, 'index.html',{'form':form})


"""
def room(request, room_name):
    User = get_user(request)
    name=User.username
    #return render(request, 'room.html' ,{'room_name': room_name},{'person_name':name})
    return render(request, 'chat.html' ,{'room_name_json': mark_safe(json.dumps(room_name)),
    'person_name':mark_safe(json.dumps(name)),
    'name':name,
    'room':room_name
    })
"""
def room(request, room_name):

    User = get_user(request)
    user_name=User.username
    room, created = Room.objects.get_or_create(name=room_name)
    print(room)
    rooms = Room.objects.all()
    search_term=''
        
    if 'search' in request.GET:
        search_term= request.GET['search']
        rooms = rooms.filter(name__icontains=search_term)
        print('######',rooms)


    room=room.name
    #print(room)
    #return render(request, 'room.html' ,{'room_name': room_name},{'person_name':name})
    return render(request, 'chat.html' ,{'room_name_json': mark_safe(json.dumps(room)),
    'person_name':mark_safe(json.dumps(user_name)),
    'name':user_name,
    'room':room,
    'rooms':rooms
    })

def search(request):
    
    print("######")
    rooms = Room.objects.all()
    
    search_term=''
    if 'name' in request.GET:
        rooms = rooms.order_by('id')
        
    if 'search' in request.GET:
        search_term= request.GET['search']
        res = rooms.filter(name__icontains=search_term)
        
    print(res,"####")
    context = {'res' : res,'search_term' : search_term}
    return render(request, 'chat.html', context)


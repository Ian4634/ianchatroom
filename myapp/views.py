from django.shortcuts import render,redirect
from .models import Message,Username,Room
# Create your views here.
def home(request):
    return render(request,'home.html')


def create(request):
    username = request.POST['username']
    room = request.POST['room']

    if Room.objects.filter(name = room).exists() and Username.objects.filter(username=username).exists():
        return redirect("/"+room+"/"+username+"/")
    elif Room.objects.filter(name = room).exists() and not(Username.objects.filter(username=username).exists()):
        new_user = Username.objects.create(username=username)
        new_user.save()
        return redirect("/"+room+"/"+username+"/")
    elif not(Room.objects.filter(name=room).exists()) and Username.objects.filter(username=username).exists():
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect("/"+room+"/"+username+"/")
    else:
        new_user = Username.objects.create(username=username)
        new_user.save()
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect("/"+room+"/"+username+"/")

def room(request,room = 'defaut',username = 'defaut'):
    messages = Message.objects.filter(room=room)
    return render(request,'room.html',{'username':username,'room':room,'messages':messages})

def send(request,room,username):
    value = request.POST['value']
    new_message = Message.objects.create(sent_user = username,value = value, room = room)
    new_message.save()
    return redirect("/"+room+"/"+username+"/")

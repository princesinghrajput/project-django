from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1, 'name':'Learn Javascript in 5 minutes'},
    {'id':2, 'name':'Learn Python in 10 minutes'},
    {'id':3, 'name':'Learn Java in 15 minutes'},
    {'id':4, 'name':'Learn C++ in 20 minutes'},
    {'id':5, 'name':'Learn C# in 25 minutes'},
    {'id':6, 'name':'Learn Go in 30 minutes'},
    {'id':7, 'name':'Learn Rust in 35 minutes'},
    {'id':8, 'name':'Learn Rust in 35 minutes'},
]




def Home(request):
    return render(request, 'base/home.html', context={'rooms':rooms})
    

def Room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
            

        context = {'room':room}
    return render(request, 'base/room.html', context)



def About(request):
    return render(request, 'base/about.html')
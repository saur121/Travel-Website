from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City Never Sleeps'
    dest1.price = 800
    dest1.img = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Pune'
    dest2.desc = 'The City of Fresh Air'
    dest2.price = 600
    dest2.img = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Silicon Value of India'
    dest3.price = 400
    dest3.img = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    
    return render(request, "index.html", {'dests': dests})

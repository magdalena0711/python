from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

import  os
def login(request):
    return render(request, 'EasyQuizzy/loginPage.html')

def find(request, room_name):
    print('usao')
    return render(request, "EasyQuizzy/finding_opponent.html", {"room_name": room_name})
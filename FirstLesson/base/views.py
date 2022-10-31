from urllib import request
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')
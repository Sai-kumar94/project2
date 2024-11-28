from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def subscribe(request):
    return HttpResponse('channel subscribed')

def unsubscribe(request):
    return HttpResponse('channel unsubscribed')

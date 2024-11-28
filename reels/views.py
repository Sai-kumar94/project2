from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def scroll(request):
    return HttpResponse('scroll to watch reels')

def stop(request):
    return HttpResponse('stop to watch a reel')

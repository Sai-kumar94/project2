from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def like(request):
    return HttpResponse('like a video')

def unlike(request):
    return HttpResponse('unlike a video')

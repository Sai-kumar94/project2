from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def send_request(request):
    return HttpResponse('friend request sent')


def confirm_request(request):
    return HttpResponse('friend request confirmed')

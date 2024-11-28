from django.urls import path
from request.views import *
urlpatterns = [
    path('send_request/',send_request,name='send_request'),
    path('confirm_request',confirm_request,name='confirm_request')
]

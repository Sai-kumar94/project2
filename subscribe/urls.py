from django.urls import path
from subscribe.views import *
urlpatterns = [
    path('subscribe/',subscribe,name='subscribe'),
    path('unsubscribe/',unsubscribe,name='unsubscribe'),

]

from django.contrib import admin
from django.urls import path
#from geosmart_club_chat.views import ContactList, ChatList, MessageList

from .views import index, room

app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    path('room/<str:room_name>/', room, name='room'),
    #path('messages/', MessageList.as_view()),
    #path('contacts/', ContactList.as_view()),
    #path('history/', ChatList.as_view())
    ]

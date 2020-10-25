# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from  django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.views.generic import ListView
from geosmart_club_chat.models import Chat, Message, Contact
from geosmart_club_chat.api.serializers import ContactSerializer, ChatSerializer, MessageSerializer
from rest_framework import mixins
from rest_framework import generics
from .models import Chat, Contact
import json

def index(request):
    return render(request, 'chat/index.html')


# @login_required   #Uncomment also auth.decorators library
def room(request, room_name):
    return render(request, 'chat/room/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })

def get_last_15_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:15]

User = get_user_model()

def get_user_contact(username):
    #user = get_object_or_404(User, username=username)
    contact = get_object_or_404(Contact,username=username)
    return contact

def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)

# class ContactList(mixins.ListModelMixin,
#                     generics.GenericAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class MessageList(mixins.ListModelMixin,
#                     generics.GenericAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class ChatList(mixins.ListModelMixin,
#                     generics.GenericAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
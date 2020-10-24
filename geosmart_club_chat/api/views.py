from rest_framework import viewsets
from geosmart_club_chat.models import Message, Chat, Contact
from .serializers import MessageSerializer, ChatSerializer, ContactSerializer
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

# class ChatViewSet(viewsets.ModelViewSet):
#     serializer_class = ChatSerializer
#     queryset = Chat.objects.all()

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()



# class MessageListView(ListAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageDetailView(RetrieveAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageCreateView(CreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageUpdateView(UpdateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageDeleteView(DestroyAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

User = get_user_model()

def get_user_contact(username):
    user = get_object_or_404(User,username = username)
    contact = get_object_or_404(Contact, user = user)
    return contact

class ChatListView(ListAPIView):
    #queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset

class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

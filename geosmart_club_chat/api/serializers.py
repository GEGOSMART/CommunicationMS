from rest_framework import serializers
from geosmart_club_chat.models import Contact, Chat, Message


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [ 'username', 'firstname', 'lastname', 'friends']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'participantes', 'messages']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'content', 'timestamp']
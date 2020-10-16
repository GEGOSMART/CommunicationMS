from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_15_messages():
        return Message.objects.order_by('-timestamp').all()[:15]

class Chat(models.Model):
    participantes = models.ManyToManyField(Contact, related_name='chats')
    messages = models.ManyToManyField(Message,blank=True)

    def __str__(self):
        return "{}".format(self.pk)
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Contact(models.Model):
    #user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    username = models.CharField(primary_key=True, default="def_user", max_length=20) #editable=False
    firstname = models.CharField(max_length=25, default='null')
    lastname = models.CharField(max_length=30, default='null')
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    author = models.ForeignKey(Contact,db_column='username', related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''+self.author.username+': '+self.content#"{}".format(self.content)



class Chat(models.Model):
    id = models.CharField(primary_key=True, max_length=25) #editable=False
    participantes = models.ManyToManyField(Contact, related_name='chats')
    messages = models.ManyToManyField(Message,blank=True)

    def __str__(self):
        return "{}".format(self.pk)
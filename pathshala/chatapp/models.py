from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Room(models.Model):

    INDIVIDUAL = 'IN'
    GROUP = 'GR'
    BUSSINESS = 'BU'

    LABEL_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (GROUP, 'Group'),
        (BUSSINESS,'Bussiness'),
        
    ]

    name = models.CharField(max_length=50,unique=True)
    label = models.CharField(max_length=20,choices=LABEL_CHOICES,default=INDIVIDUAL,)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages',on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('timestamp').all()[:10]


from django.db.models import (Model, TextField, DateTimeField, ForeignKey,
                              CASCADE)
from datetime import datetime, timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
import time
import pytz
User = get_user_model()
from django.shortcuts import render




# def get_users(request):
#     #users = db.child("users").get()
#     return render(request, 'users.html', {'users': User.val()})


class MessageModel(Model):
    """
    This class represents a chat message. It has a owner (user), timestamp and
    the message body.

    """
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='user',
                      related_name='from_user', db_index=True)
    recipient = ForeignKey(User, on_delete=CASCADE, verbose_name='recipient',
                           related_name='to_user', db_index=True)
    timestamp = DateTimeField('timestamp', auto_now_add=True, editable=False,
                              db_index=True)
    body = TextField('body')

    def __str__(self):
        return str(self.id)

    def characters(self):
        """
        Toy function to count body characters.
        :return: body's char number
        """
        return len(self.body)

    def notify_ws_clients(self):
        """
        Inform client there is a new message.
        """
        notification = {
            'type': 'recieve_group_message',
            'message': '{}'.format(self.id)
        }

        channel_layer = get_channel_layer()
        print("user.id {}".format(self.user.id))
        print("user.id {}".format(self.recipient.id))

        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    def save(self, *args, **kwargs):
        """
        Trims white spaces, saves the message and notifies the recipient via WS
        if the message is new.
        """
        new = self.id
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(MessageModel, self).save(*args, **kwargs)
        ##############Firebase#################
        
        # tz = pytz.timezone('Asia/Kolkata')
        # utc_dt = datetime.now(timezone.utc).astimezone(tz)
        # millis = int(time.mktime(utc_dt.timetuple()))

        # data = {"sender": self.user.username,"recipient":self.recipient.username,"msg":self.body,"time":millis}
        # database.child("Messages").child(self.id).set(data)
        ########################################
        if new is None:
            self.notify_ws_clients()

    # Meta
    class Meta:
        app_label = 'core'
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)

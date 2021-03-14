from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from core.models import MessageModel
from rest_framework.serializers import ModelSerializer, CharField
#import pyrebase
from datetime import datetime,timedelta
User = get_user_model()


class MessageModelSerializer(ModelSerializer):
    user = CharField(source='user.username', read_only=True)
    recipient = CharField(source='recipient.username')
    

    def create(self, validated_data):
        user = self.context.get("request").user
        recipient = get_object_or_404(
            User, username=validated_data['recipient']['username'])
        msg = MessageModel(recipient=recipient,
                           body=validated_data['body'],
                           user=user)

        #user = self.context['request'].user
        # data = self.context['request'].data
        # recipient = data['recipient']
        # msg = data['body']
        
        # #print(user)
        
        
        # now = datetime.utcnow()+timedelta(hours=5.5)
        # monthNames = ["Jan", "Feb", "March", "April", "May", "June",
        # "July", "August", "Sep", "Oct", "Nov", "Dec"]
        # month = monthNames[int(now.strftime('%m '))-1]
        # dd = now.strftime('%d')
        # year =now.strftime('%Y')
        # date = month + " " +dd + "," + year
        # time = now.strftime('%I:%M %p')

        msg.save()
        return msg

    class Meta:
        model = MessageModel
        fields = ('id', 'user', 'recipient', 'timestamp', 'body')
        


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        

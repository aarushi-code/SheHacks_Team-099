# from django.http import HttpResponse
# from django.shortcuts import render
# import pyrebase
# #from firebase import firebase
# from django.contrib import auth
# #admin_uid = "tSSv32i3usbppGZUIxsdXczf9NM2"
# name = " "
# email = " "


# config = {
#   'apiKey': "AIzaSyCx1vQuzwNNi1Q9bjPw1qnUyk9gdydvzpU",
#   'authDomain': "chat-91bbb.firebaseapp.com",
#   'databaseURL': "https://chat-91bbb.firebaseio.com",
#   'projectId': "chat-91bbb",
#   'storageBucket': "chat-91bbb.appspot.com",
#   'messagingSenderId': "120170902173",
#   'appId': "1:120170902173:web:6b76957bbce2ea7469da74"
# }
# firebase = pyrebase.initialize_app(config)

# auth = firebase.auth()
# database = firebase.database()

# def home(request):
#   uid = request.session['fav_color']
#   names=[]
#   j=0
#   #user = auth.get_user(uid)
#   all_user_ids = database.child("Accounts").child('').shallow().get().val()
#   all_user_ids = list(all_user_ids)
#   print(all_user_ids)
#   print(database.child("Accounts").child(all_user_ids[0]).child('name').shallow().get())
#   # for i in all_user_ids:
#   #   names[j]= database.child("Accounts").child(i).get('name')
#   #   j+=1

#   print('Successfully fetched user data: {0}'.format(uid))
#   print(names)
#   return (all_user_ids)
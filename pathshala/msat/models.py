from django.db import models
#from login.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


class MSAT(models.Model):
    #r_id = models.IntegerField()
    #stud_id = models.CharField(max_length = 50)
    response = models.CharField(max_length = 500)
    timestamp = models.IntegerField()  # To store duration in seconds
    mark_scored = models.IntegerField()
    answered = models.CharField(max_length = 500)
    #email= models.EmailField(max_length = 200, default='xx@xx.com')
    def __str__(self):
        return self.response
from django.db import models

# Create your models here.

class questions(models.Model):
    id = models.AutoField(primary_key=True) 
    description = models.CharField(max_length=255)
    questions_img = models.ImageField(upload_to = "questions_img/%Y/%m/%d/") 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return str(self.id)

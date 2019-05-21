from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class lmode(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    pic_image = models.ImageField(upload_to='media',blank=True)
    comment = models.TextField()
    def __str__(self):
        return self.username

class userp(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    def __str__(self):
        return self.user.username

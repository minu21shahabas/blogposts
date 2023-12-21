from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class bloguser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobileno=models.CharField(max_length=255)
class newpost(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    bimg=models.ImageField(upload_to="image/",null=True)
    recipe=models.TextField(null=True)



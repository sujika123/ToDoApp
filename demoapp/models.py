from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user=models.BooleanField(default=False)

class userlogin(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(max_length=200)
    image=models.ImageField()

    def __str__(self):
        return self.name

# Event
class eventadd(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=30)
    date=models.DateField()
    description=models.TextField(max_length=200,null=True,blank=True)
    image=models.ImageField()


    def __str__(self):
        return self.name

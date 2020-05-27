from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Members(models.Model):
    First_Name = models.CharField(max_length = 150)
    Last_Name = models.CharField(max_length = 150)
    Email = models.EmailField(max_length = 250, unique = True)

    def __str__(self):
        return str(self.First_Name+" "+self.Last_Name)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='form_app/profile_pics', blank = True)

    def __str__(self):
        return self.user.username

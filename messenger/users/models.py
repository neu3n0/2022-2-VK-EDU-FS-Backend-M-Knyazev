from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()


class User(AbstractUser):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # contacts ManyToMany на самого себя?
    contacts = models.ManyToManyField('User')

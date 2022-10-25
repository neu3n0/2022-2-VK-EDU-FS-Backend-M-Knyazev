from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    age = models.IntegerField(null=True, blank=True, default=None)
    mobile = models.IntegerField(null=False, blank=False, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f'User {self.profile_user.username} profile'


class User(AbstractUser):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='profile_user')
    # contacts ManyToMany на самого себя?
    contacts = models.ManyToManyField('User')

    def __str__(self) -> str:
        return f'User {self.username}'
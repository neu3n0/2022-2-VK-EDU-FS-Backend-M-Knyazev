from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    contacts = models.ManyToManyField('User')
    age = models.IntegerField(null=True, blank=True, default=None)
    mobile = models.CharField(max_length=12, null=False, blank=False, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f'User {self.username}'
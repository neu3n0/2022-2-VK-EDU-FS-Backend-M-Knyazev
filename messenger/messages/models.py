from operator import mod
from django.db import models
from users import User

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
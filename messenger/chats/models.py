from django.db import models
from users.models import User
# from messages.models import Message

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # message = models.ForeignKey(Message, on_delete=models.CASCADE)
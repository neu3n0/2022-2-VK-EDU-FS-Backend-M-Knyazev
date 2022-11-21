from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Возраст'
    )
    mobile = models.CharField(
        max_length=12,
        unique=True,
        verbose_name='Номер телефона'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'User {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Contactbook(models.Model):
    owner = models.OneToOneField(User, verbose_name='Владелец', related_name='contactbook', on_delete=models.CASCADE)
    contacts = models.ManyToManyField(User, verbose_name='Контакты', related_name='bookcontacts')

    class Meta:
        verbose_name = 'Контактная книга'
        verbose_name_plural = 'Контактные книги'
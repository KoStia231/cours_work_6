from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    first_name = models.CharField(verbose_name='имя', max_length=30, unique=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    phone_number = models.IntegerField(verbose_name='Телефон', **NULLABLE)
    token = models.CharField(max_length=255, **NULLABLE, verbose_name='Токен')
    new_password = models.CharField(verbose_name='Новый пароль', max_length=100, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        permissions = [
            ('manager', 'Может просматривать список пользователей сервиса и блокировать пользователей сервиса')
        ]

# Create your models here.

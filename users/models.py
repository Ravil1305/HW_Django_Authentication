import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона')
    country = models.CharField(max_length=30, verbose_name='Страна')
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.UUIDField(null=True, default=uuid.uuid4)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

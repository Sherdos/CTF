from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    machine = models.ForeignKey('tasks.Machine', on_delete=models.CASCADE, verbose_name='Машина', related_name='users', null=True)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = UserManager()

    REQUIRED_FIELDS = ["email", ]

    def full_name(self):
        return self.name + " " + self.last_name

    def __str__(self):
        return self.username

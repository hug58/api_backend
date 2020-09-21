from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    username = models.TextField(unique=True)
    email = models.EmailField()
    name = models.TextField()
    last_name = models.TextField()
    status = models.TextField(null=True)
    city = models.TextField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = UserManager()

    REQUIRED_FIELDS = ["email", ]

    def full_name(self):
        return self.name + " " + self.last_name

    def __str__(self):
        return self.username

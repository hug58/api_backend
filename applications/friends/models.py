from django.db import models
from django.conf import settings
from .managers import FriendsManagers
# Create your models here.


class Friends(models.Model):
    name = models.TextField()
    last_name = models.TextField()
    status = models.TextField(null=True)
    city = models. TextField(null=True)
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    objects = FriendsManagers()

    def __str__(self):
        return self.name+" " + self.last_name


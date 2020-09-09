from django.db import models
from django.conf import settings
# Create your models here.


class Friends(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    city = models.CharField(max_length=15)

    def __str__(self):
        return self.name+" " + self.last_name

    """
    friend = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="prod_created",
    )
    """
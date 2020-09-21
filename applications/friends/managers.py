from django.db import models


class FriendsManagers(models.Manager):

    def list_friends_users(self, username):
        return self.filter(friend__username=username).order_by("name")

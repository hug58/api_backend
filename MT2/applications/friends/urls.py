from django.urls import path
from . import views

app_name = "friends_app"

urlpatterns = [
    path(
        'list_friends/<username>',
        views.ListFriends.as_view(),
        name='list_friends'
    ),
]
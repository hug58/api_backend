from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path(
        'register',
        views.RegisterUser.as_view(),
        name='register'
    ),
    path(
        'list',
        views.ListUsers.as_view(),
        name='list_users'
    ),
]
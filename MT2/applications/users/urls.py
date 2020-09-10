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
        'register2',
        views.RegisterUser2.as_view(),
        name='register'
    )
]
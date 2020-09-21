from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path(
        'register_user',
        views.RegisterUser.as_view(),
        name='register_user'
    ),
    path(
        'all_user/excel',
        views.Data.as_view(),
        name='all_user'
    )
]
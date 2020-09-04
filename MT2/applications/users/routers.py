from rest_framework.routers import DefaultRouter

from . import viewsets
router = DefaultRouter()

router.register(r'users_register', viewsets.UserViewSet, basename="users_register")

urlpatterns = router.urls
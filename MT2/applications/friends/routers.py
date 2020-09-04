from rest_framework.routers import DefaultRouter

from . import viewsets
router = DefaultRouter()

router.register(r'friends_register', viewsets.FriendsViewSet, basename="friends_register")

urlpatterns = router.urls
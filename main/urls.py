from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LobbyViewSet, MoveViewSet

from . import views
router = DefaultRouter()
router.register('lobbies', LobbyViewSet)
router.register('moves', MoveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import LobbyViewSet, MoveViewSet
from register import views as v


router = DefaultRouter()
router.register('lobbies', LobbyViewSet)
router.register('moves', MoveViewSet)

urlpatterns = [
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("register/", v.register, name="register"),  # <-- added
    # path('', include("django.contrib.auth.urls")),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]

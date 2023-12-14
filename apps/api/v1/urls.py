from django.urls import include, path
from rest_framework import routers

from .users.views import UserViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UserViewset, basename="users")

urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]

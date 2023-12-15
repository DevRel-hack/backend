from django.urls import include, path
from rest_framework import routers

from .attributes.views import AttributesView
from .events.views import EventViewset, EventTypeViewset
from .specialists.views import SpecialistsViewset
from .users.views import UserViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UserViewset, basename="users")
router.register("specialists", SpecialistsViewset, basename="specialists")
router.register("events", EventViewset, basename="events")
router.register("event_types", EventTypeViewset, basename="event_types")


urlpatterns = [
    path("attributes", AttributesView.as_view(), name="attributes"),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]

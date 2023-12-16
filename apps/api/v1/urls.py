from django.urls import include, path
from rest_framework import routers

from .attributes.views import AttributesView
from .events.views import (
    EventViewset,
    ListCreateParticipantView,
    ParticipantObjView,
)
from .specialists.views import SpecialistsViewset
from .users.views import UserViewset

app_name = "api"

router = routers.DefaultRouter()
router.register("users", UserViewset, basename="users")
router.register("specialists", SpecialistsViewset, basename="specialists")
router.register("events", EventViewset, basename="events")


urlpatterns = [
    path("attributes", AttributesView.as_view(), name="attributes"),
    path(
        "events/<int:event_id>/participants/",
        ListCreateParticipantView.as_view(),
        name="parts",
    ),
    path(
        "events/<int:event_id>/participants/<int:pk>",
        ParticipantObjView.as_view(),
        name="parts",
    ),
    path("auth/", include("djoser.urls.jwt")),
    path("", include(router.urls)),
]

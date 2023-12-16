from rest_framework import serializers

from apps.events.models import Event
from apps.events.services import add_event, edit_event

from ..attributes.serializers import EventStatusSerializer, TagSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "status",
            "title",
            "description",
            "start_at",
            "is_internal",
            "form",
            "place",
            "url",
            "tags",
            "comments",
        )

    def create(self, validated_data):
        return add_event(data=validated_data)

    def update(self, instance, validated_data):
        return edit_event(instance, validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["status"] = EventStatusSerializer(instance.status).data
        rep["tags"] = TagSerializer(instance.tags, many=True).data
        return rep

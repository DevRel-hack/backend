from rest_framework import serializers

from apps.events.models import Event, EventType

from apps.events.services import add_event, edit_event


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ("id", "title")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "status",
            "title",
            "start_at",
            "form",
            "place",
            "type",
            "themes",
        )

    def create(self, validated_data):
        return add_event(data=validated_data)

    def update(self, instance, validated_data):
        return edit_event(instance, validated_data)

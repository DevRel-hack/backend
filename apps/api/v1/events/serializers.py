from rest_framework import serializers

from apps.events.models import Event, Participant
from apps.events.services import add_event, edit_event

from ..attributes.serializers import EventStatusSerializer, TagSerializer


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("id", "specialist", "role", "comment")


class BaseEventSerializer(serializers.ModelSerializer):
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
        return


class ListEventSerializer(BaseEventSerializer):
    status = EventStatusSerializer()
    tags = TagSerializer()


class RetrieveEventSerializer(BaseEventSerializer):
    # key_parts = ParticipantSerializer(many=True)

    class Meta(BaseEventSerializer.Meta):
        # fields = BaseEventSerializer.Meta.fields + ("key_parts",)
        fields = BaseEventSerializer.Meta.fields


class CreateEditEventSerializer(BaseEventSerializer):
    def to_representation(self, instance):
        return RetrieveEventSerializer(instance).data

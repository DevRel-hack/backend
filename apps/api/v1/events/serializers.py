from rest_framework import serializers

from apps.events.models import Event, Participant
from apps.events.services import add_event, edit_event
from apps.specialists.models import Specialist

from ..attributes.serializers import (
    EventStatusSerializer,
    TagSerializer,
    RoleSerializer,
)


class ShortSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ("id", "first_name", "last_name", "company", "phone", "email")


class BaseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("id", "specialist", "role", "comment")


class ParticipantSerializer(BaseParticipantSerializer):
    role = RoleSerializer()
    specialist = ShortSpecialistSerializer()


class CreateParticipantSerializer(BaseParticipantSerializer):
    def to_representation(self, instance):
        return ParticipantSerializer(instance).data


class EditParticipantSerializer(BaseParticipantSerializer):
    class Meta(BaseParticipantSerializer.Meta):
        read_only_fields = ("specialist",)

    def to_representation(self, instance):
        return ParticipantSerializer(instance).data


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


class ListEventSerializer(BaseEventSerializer):
    status = EventStatusSerializer()
    tags = TagSerializer(many=True)


class RetrieveEventSerializer(BaseEventSerializer):
    participants = ParticipantSerializer(many=True)

    class Meta(BaseEventSerializer.Meta):
        fields = BaseEventSerializer.Meta.fields + ("participants",)


class CreateEditEventSerializer(BaseEventSerializer):
    def to_representation(self, instance):
        return RetrieveEventSerializer(instance).data


class BaseParticipantSerializer(serializers.ModelSerializer):
    """Базовый сериализатор Участника."""

    class Meta:
        model = Participant
        fields = ("id", "specialist", "role", "comment")

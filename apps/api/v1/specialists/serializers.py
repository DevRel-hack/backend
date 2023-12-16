from rest_framework import serializers

from apps.events.models import Event, Participant
from apps.specialists.crud import specialist_exists
from apps.specialists.models import Specialist
from apps.specialists.services import add_specialist, edit_specialist

from ..attributes.serializers import (
    ToolSerializer,
    CitySerializer,
    JobSerializer,
    GradeSerializer,
    RoleSerializer,
)


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "is_colleague",
            "city",
            "job",
            "grade",
            "tools",
        )

    def validate_email(self, value):
        if self.instance is None and specialist_exists(email=value):
            raise serializers.ValidationError(
                "Специалист с таким email уже добавлен."
            )
        return value

    def create(self, validated_data):
        return add_specialist(data=validated_data)

    def update(self, instance, validated_data):
        return edit_specialist(instance, validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["tools"] = ToolSerializer(instance.tools, many=True).data
        rep["city"] = CitySerializer(instance.city).data
        rep["job"] = JobSerializer(instance.job).data
        rep["grade"] = GradeSerializer(instance.grade).data
        return rep


class ShortEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "start_at")


class ParticipantInSpecSerializer(serializers.ModelSerializer):
    event = ShortEventSerializer()
    role = RoleSerializer()

    class Meta:
        model = Participant
        fields = ("id", "event", "role", "comment")


class RetrieveSpecialistSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    job = JobSerializer()
    grade = GradeSerializer()
    tools = ToolSerializer(many=True)
    participants = ParticipantInSpecSerializer(many=True)

    class Meta:
        model = Specialist
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "is_colleague",
            "city",
            "job",
            "grade",
            "tools",
            "participants",
        )

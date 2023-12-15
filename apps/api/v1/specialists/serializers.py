from rest_framework import serializers

from apps.specialists.crud import specialist_exists
from apps.specialists.models import Specialist
from apps.specialists.services import add_specialist, edit_specialist


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            "id",
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

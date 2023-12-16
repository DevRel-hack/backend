from rest_framework import serializers

from apps.attributes.models import (
    City,
    Tool,
    Job,
    Grade,
    Tag,
    EventStatus,
    Role,
)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "title")


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ("id", "title")


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "title")


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ("id", "title")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ("id", "title")


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "title")


class AttributesSerializer(serializers.Serializer):
    """Сериализация полей списков всех атрибутов."""

    cities = CitySerializer(many=True)
    tools = ToolSerializer(many=True)
    jobs = JobSerializer(many=True)
    grades = GradeSerializer(many=True)
    tags = TagSerializer(many=True)
    statuses = EventStatusSerializer(many=True)
    roles = RoleSerializer(many=True)

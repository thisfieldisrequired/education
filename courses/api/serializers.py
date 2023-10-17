from rest_framework import serializers
from courses.models import Subject, Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
    """Сериализация предмета"""

    class Meta:
        model = Subject
        fields = ["id", "title", "slug"]


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализация занятия"""

    class Meta:
        model = Module
        fields = ["order", "title", "description"]


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация курса"""

    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "title",
            "slug",
            "overview",
            "created",
            "owner",
            "modules",
        ]


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    """Сериализация содержимого занятий"""

    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ["order", "item"]


class ModuleWithContentSerializer(serializers.ModelSerializer):
    """Сериализация модуля курса с содержимым занятий"""

    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = ["order", "title", "description", "contents"]


class CourseWithContentSerializer(serializers.ModelSerializer):
    """Сериализация курса с содержимым модуля"""

    modules = ModuleWithContentSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "title",
            "slug",
            "overview",
            "created",
            "owner",
            "modules",
        ]

from rest_framework import serializers

from ..models import Subject, Course, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
    """Предметы"""

    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    """Модули"""

    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    """Курсы"""

    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']


class ItemRelatedField(serializers.ModelSerializer):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    """Контент модуля"""

    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentsSerializer(serializers.ModelSerializer):
    """Модули с контентом"""

    contents = ContentSerializer(many=True)

    class Meta:
        model= Module
        fields = ['order', 'title', 'description', 'contents']


class CourseWithContentsSerializer(serializers.ModelSerializer):
    """Курсы с контентом"""

    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug', 'overview', 'created', 'owner', 'modules']

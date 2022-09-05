from rest_framework import serializers
from notes.models import Note, Tag


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["content", "tags", "date_created", "date_modified"]
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

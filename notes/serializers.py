from rest_framework import serializers
from notes.models import Note, Tag


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["content", "tags"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

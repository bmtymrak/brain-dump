from notes.serializers import NoteSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class NotesListView(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

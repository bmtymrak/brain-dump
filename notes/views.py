from notes.serializers import NoteSerializer, TagSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from notes.models import Note, Tag


class NoteList(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        print(self.request.user.notes.all())
        serializer.save(user=self.request.user)


class NoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


class TagList(ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permissions_classes = [IsAuthenticated]

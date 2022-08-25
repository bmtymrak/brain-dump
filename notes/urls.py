from django.urls import path
from notes.views import NoteList, NoteDetail, TagList


urlpatterns = [
    path("notes/", NoteList.as_view()),
    path("notes/<int:pk>", NoteDetail.as_view()),
    path("tags/", TagList.as_view()),
]

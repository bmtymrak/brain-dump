from django.urls import path
from notes.views import NoteList, NoteDetail, TagList


urlpatterns = [
    path("", NoteList.as_view()),
    path("<int:pk>", NoteDetail.as_view()),
    path("tags/", TagList.as_view()),
]

from django.contrib import admin
from notes.models import Note, Tag


admin.site.register(Note)
admin.site.register(Tag)

from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(blank=False, max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tags",
        on_delete=models.CASCADE,
        null=False,
    )


class Note(models.Model):
    content = models.TextField(
        blank=True,
    )
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="notes",
        on_delete=models.CASCADE,
        null=False,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

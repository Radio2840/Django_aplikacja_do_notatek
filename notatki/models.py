from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


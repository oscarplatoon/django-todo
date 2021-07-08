from django.db import models
from django.conf import settings


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)  # author links to the auth_user table in the db. linked automatically using the ids

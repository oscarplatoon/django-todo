from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"ID: {self.id} Title: {self.title}"
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f"Title: {self.title}"


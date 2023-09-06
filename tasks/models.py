from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        User,
        related_name="tasks",
        on_delete=models.CASCADE,
    )

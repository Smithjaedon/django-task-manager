from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS_CHOICES = [("Done", "Done"), ("In Progress", "In Progress"), ("To Do", "To Do")]


# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="tasks", null=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="To Do")

    def __str__(self):
        return self.title


class User(AbstractUser):
    def __str__(self):
        return self.username

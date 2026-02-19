from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.CharField(max_length=35)
    desc = models.TextField(max_length=150)
    completed = models.BooleanField(default=False)
    trashed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank= True)
    def __str__(self):
        return self.task

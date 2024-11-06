from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Task(models.Model):

    STATUS_CHOICES = [
        ('uncompleted','Uncompleted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    task_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500,null=True,blank=True)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todos')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='uncompleted')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

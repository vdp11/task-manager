from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings 

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('activated', 'Activated'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

# Create your models here.

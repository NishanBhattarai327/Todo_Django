from django.db import models
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    PRIORITY_TYPE_CHOICE = [
        ('LO', 'LOW'),
        ('MD', 'MEDIUM'),
        ('HI', 'HIGH')
    ]
    task = models.TextField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    prority = models.CharField(max_length=2, choices=PRIORITY_TYPE_CHOICE, default='LO')

    def __str__(self):
        return self.task[:10]

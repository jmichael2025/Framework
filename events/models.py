from django.db import models

# Create your models here.
from django.db import models


class Event(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('social', 'Social'),
        ('sports', 'Sports'),
        ('career', 'Career'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    organizer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models


from django.contrib.auth.models import User


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

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'event'],
                name='unique_user_event_registration'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
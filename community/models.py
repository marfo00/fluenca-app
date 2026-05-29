from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200, default="Church Auditorium")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Recording(models.Model):
    CATEGORY_CHOICES = [
        ('sunday', 'Sunday Service'),
        ('revival', 'Revival & Power Session'),
        ('teaching', 'Teaching'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    video_url = models.URLField(blank=True, null=True)
    audio_url = models.URLField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date})"


class Song(models.Model):
    title = models.CharField(max_length=200)
    lyrics = models.TextField(blank=True)
    audio_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Challenge(models.Model):
    CATEGORY_CHOICES = [
        ('bible', 'Bible Reading'),
        ('outreach', 'Social Media Outreach'),
        ('gospel', 'Gospel Sharing'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    points_reward = models.IntegerField(default=10)
    active_until = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"

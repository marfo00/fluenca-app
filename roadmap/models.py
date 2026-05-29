from django.db import models
from django.conf import settings

class RoadmapLevel(models.Model):
    LEVEL_CHOICES = [
        ('new_convert', 'New Convert'),
        ('growing', 'Growing Believer'),
        ('established', 'Established Believer'),
        ('mature', 'Mature Disciple'),
        ('leader', 'Kingdom Leader'),
    ]
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES, unique=True)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Sermon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)
    audio_url = models.URLField(blank=True, null=True)
    level = models.ForeignKey(RoadmapLevel, on_delete=models.SET_NULL, null=True, related_name='sermons')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('evangelism', 'Evangelism Skills'),
        ('preaching', 'Preaching Skills'),
        ('prayer', 'Prayer & Intercession'),
        ('relationships', 'Strategic Relationships'),
        ('favor', 'Commanding Favor'),
        ('tarrying', 'Tarrying'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} — {self.title}"


class ChristianBriefcase(models.Model):
    CATEGORY_CHOICES = [
        ('practice', 'Practice'),
        ('history', 'History'),
        ('wisdom', 'Wisdom Key'),
        ('story', 'Story of Influence'),
        ('devotional', 'Devotional'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} — {self.title}"

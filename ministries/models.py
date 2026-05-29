from django.db import models

MINISTRY_CHOICES = [
    ('youth', 'Youth Ministry'),
    ('women', "Women's Ministry"),
    ('pemem', 'PEMEM'),
    ('children', 'Children Ministry'),
    ('ham', 'HAM'),
]

class Ministry(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='ministry_logos/', null=True, blank=True)
    gradient_start = models.CharField(max_length=20, default='#1d4ed8')
    gradient_end = models.CharField(max_length=20, default='#60a5fa')
    
    class Meta:
        verbose_name_plural = 'Ministries'

    def __str__(self):
        return self.name

class MinistryPost(models.Model):
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ministry.name} — {self.title}"

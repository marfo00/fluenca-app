from django.db import models
from django.conf import settings

class Post(models.Model):
    POST_TYPES = [
        ('verse', 'Daily Verse'),
        ('news', 'Gospel News'),
        ('testimony', 'Testimony'),
        ('announcement', 'Announcement'),
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='news')
    content = models.TextField()
    scripture_reference = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed URL")
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author.username} - {self.post_type} ({self.created_at.date()})"

    def like_count(self):
        return self.reactions.filter(reaction_type='like').count()

class Reaction(models.Model):
    REACTION_TYPES = [
        ('like', '👍'),
        ('amen', '🙏'),
        ('fire', '🔥'),
        ('heart', '❤️'),
        ('praise', '🙌'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.CharField(max_length=10, choices=REACTION_TYPES, default='like')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} reacted {self.reaction_type} on {self.post.id}"

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username} on Post {self.post.id}"

class DailyVerse(models.Model):
    verse_text = models.TextField()
    scripture_reference = models.CharField(max_length=100)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube embed URL for 'Cultivate a rhythm' section")
    date = models.DateField(unique=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.scripture_reference} - {self.date}"

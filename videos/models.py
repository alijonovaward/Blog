from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class VideoLesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(help_text="YouTube URL yoki video fayl linki")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_standalone = models.BooleanField(default=False)

    def __str__(self):
        return self.title

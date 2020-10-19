from django.db import models
import uuid

class Videos(models.Model):
    """
    Videos model to store all youtube videos related data
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256,null=True)
    video_id = models.CharField(max_length=256,null=True, default=None, unique=True)
    channel_title = models.CharField(max_length=256,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (self.title)
    

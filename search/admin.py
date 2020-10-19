from django.contrib import admin
from .models import Videos

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'video_id', 'channel_title')
    ordering = ('-created',)
    search_fields = ('title',)
    list_filter = ('title', 'created',)


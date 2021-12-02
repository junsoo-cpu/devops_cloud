from django.contrib import admin
from music.models import Video

class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)

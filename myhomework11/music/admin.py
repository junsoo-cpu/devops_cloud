from django.contrib import admin
from music.models import List

class ListAdmin(admin.ModelAdmin):
    list_display = ["name", "singer", "created_at"]
    search_fields = ["name"]

admin.site.register(List, ListAdmin)


from django.contrib import admin
from ski.models import Resort

@admin.register(Resort)
class ResortAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "latitude", "longitude", "telephone"]
    list_display_links = ["name"]

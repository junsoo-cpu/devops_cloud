from django.contrib import admin

from ski.models import Resort


class ResortAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "latitude", "longitude", "telephone"]
    list_display_links = ["name"]

admin.site.register(Resort, ResortAdmin)
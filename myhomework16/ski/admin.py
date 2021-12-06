from django.contrib import admin
from ski.models import Resort

@admin.register(Resort)
class ResortAdmin(admin.ModelAdmin):
    pass


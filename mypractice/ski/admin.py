from django.contrib import admin

from ski.models import Resort


class ResortAdmin(admin.ModelAdmin):
    pass


admin.site.register(Resort)  # 등록

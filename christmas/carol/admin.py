from django.contrib import admin

from carol.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    pass


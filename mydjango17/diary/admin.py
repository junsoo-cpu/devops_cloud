from django.contrib import admin
from diary.models import Post, Comment, Tag


@admin.register(Post)  # 장식자
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)  # 장식자
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)  # 장식자
class TagAdmin(admin.ModelAdmin):
    pass

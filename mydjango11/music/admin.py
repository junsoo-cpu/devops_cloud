from django.contrib import admin
from .models import List
from django.contrib.auth.models import User

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'singer', 'date', 'appraisal']
    list_display_links = ['name', 'singer']
    actions = ['make_published', 'make_draft']

    # admin action 추가
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}개 관심 리스트'.format(updated_count))
    make_published.short_description = '관심 리스트에 추가'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') #queryset.update
        self.message_user(request, '{}개 즐겨 찾기'.format(updated_count))
    make_draft.short_description = '즐겨 찾기'



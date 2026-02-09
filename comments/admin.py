from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_preview', 'content_object', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'content')

    def content_preview(self, obj):
        return obj.content[:50]  # faqat 50 ta belgi ko‘rsatadi little change for the test
    content_preview.short_description = 'Komment'


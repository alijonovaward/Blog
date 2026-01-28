from django.contrib import admin
from .models import Article, Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ("author", "tags")
    search_fields = ("title", "content")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

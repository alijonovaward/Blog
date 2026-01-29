from django.contrib import admin
from .models import VideoLesson, Tag, Course

@admin.register(VideoLesson)
class VideoLessonAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ("author", "tags")
    search_fields = ("title", "description")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "author", "created_at")
    search_fields = ("title", "description")
    list_filter = ("author", "tags")
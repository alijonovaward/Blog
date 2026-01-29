from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from .models import VideoLesson, Course

from comments.models import Comment

def video_list(request):
    videos = VideoLesson.objects.filter(is_standalone=True).order_by("-created_at")
    courses = Course.objects.filter(is_published=True).order_by("-created_at")

    contex = {
        "videos": videos,
        "courses": courses
    }

    return render(request, "videos/video_list.html", contex)


def video_detail(request, pk):
    video = get_object_or_404(VideoLesson, pk=pk)

    video.views_count += 1
    video.save(update_fields=["views_count"])

    # Kommentlarni olish
    content_type = ContentType.objects.get_for_model(VideoLesson)
    comments = Comment.objects.filter(
        content_type=content_type,
        object_id=video.id
    ).select_related('user').order_by('-created_at')

    return render(request, "videos/video_detail.html", {
        "video": video,
        "comments": comments
    })

def course_detail(request, pk):
    videos = Course.objects.get(pk=pk).lessons.all()
    course = get_object_or_404(Course, pk=pk)
    contex = {
        "videos": videos,
        "course": course
    }

    return render(request, "videos/course_detail.html", contex)
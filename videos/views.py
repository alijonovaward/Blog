from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from .models import VideoLesson

from comments.models import Comment

def video_list(request):
    videos = VideoLesson.objects.all().order_by("-created_at")
    return render(request, "videos/video_list.html", {"videos": videos})


def video_detail(request, pk):
    video = get_object_or_404(VideoLesson, pk=pk)

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
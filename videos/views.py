from django.shortcuts import render, get_object_or_404
from .models import VideoLesson

def video_list(request):
    videos = VideoLesson.objects.all().order_by("-created_at")
    return render(request, "videos/video_list.html", {"videos": videos})

def video_detail(request, pk):
    video = get_object_or_404(VideoLesson, pk=pk)
    return render(request, "videos/video_detail.html", {"video": video})

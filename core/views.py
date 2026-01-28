from django.shortcuts import render
from articles.models import Article
from videos.models import VideoLesson
from django.db.models import Q

def home(request):
    # Oxirgi 5 ta article va video
    latest_articles = Article.objects.all().order_by("-created_at")[:5]
    latest_videos = VideoLesson.objects.all().order_by("-created_at")[:5]
    return render(request, "core/home.html", {
        "latest_articles": latest_articles,
        "latest_videos": latest_videos,
    })

def search(request):
    query = request.GET.get("q", "")
    articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    videos = VideoLesson.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, "core/search.html", {
        "query": query,
        "articles": articles,
        "videos": videos
    })

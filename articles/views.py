from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404

from comments.models import Comment
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "articles/article_list.html", {"articles": articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    content_type = ContentType.objects.get_for_model(Article)
    comments = Comment.objects.filter(
        content_type=content_type,
        object_id=article.id
    ).select_related('user').order_by('-created_at')

    context = {
        "article": article,
        "comments": comments,
    }
    return render(request, "articles/article_detail.html", context)

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from django.contrib.contenttypes.models import ContentType

@login_required
def add_comment(request, app_label, model_name, object_id):
    if request.method == "POST":
        text = request.POST.get("content")
        content_type = ContentType.objects.get(app_label=app_label, model=model_name)
        comment = Comment.objects.create(
            user=request.user,
            content=text,
            content_type=content_type,
            object_id=object_id
        )
    return redirect(request.META.get("HTTP_REFERER", "/"))

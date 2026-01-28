from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
    path("", article_list, name="article_list"),
    # path("", article_detail, name="home"),
    path("<int:pk>/", article_detail, name="article_detail"),
]

from django.urls import path
from .views import video_list, video_detail

urlpatterns = [
    path("", video_list, name="video_list"),
    path("<int:pk>/", video_detail, name="video_detail"),
    path("course/<int:pk>/", video_list, name="course_list"),
]

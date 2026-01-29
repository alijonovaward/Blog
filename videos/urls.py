from django.urls import path
from .views import video_list, video_detail, course_detail

urlpatterns = [
    path("", video_list, name="video_list"),
    path("<int:pk>/", video_detail, name="video_detail"),
    path("course/<int:pk>/", course_detail, name="course_list"),
]

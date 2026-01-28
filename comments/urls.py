from django.urls import path
from .views import add_comment

urlpatterns = [
    path("add/<str:app_label>/<str:model_name>/<int:object_id>/", add_comment, name="add_comment"),
]

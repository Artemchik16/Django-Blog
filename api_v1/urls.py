from django.urls import path

from api_v1.views import PostsList

app_name = "api_v1"

urlpatterns = [
    path("posts/", PostsList.as_view()),
    path("posts/<int:post_id>", PostsList.as_view()),
]

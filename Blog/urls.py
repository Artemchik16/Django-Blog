from django.urls import path

from Blog.views import MainPage, PostDetail

app_name = "Blog"

urlpatterns = [
    path("", MainPage.as_view(), name="main_page"),
    path("post/<int:post_id>", PostDetail.as_view(), name="post_detail"),
]

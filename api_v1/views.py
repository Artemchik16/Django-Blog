from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Blog.models import Posts

from .serializers import PostsSerializer


class PostsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class PostsList(ListAPIView):
    queryset = Posts.objects.all()

    serializer_class = PostsSerializer
    pagination_class = PostsPagination

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        if post_id:
            return Posts.objects.filter(id=post_id)
        else:
            return Posts.objects.all().order_by("-created_at")


# class PostsList(APIView):
#     def get(self, request, post_id=None):
#         if post_id:
#             post_instance = get_object_or_404(Posts, id=post_id)
#             post_serializer = PostsSerializer(post_instance)
#         else:
#             all_posts = Posts.objects.all().order_by('-created_at')
#             post_serializer = PostsSerializer(all_posts, many=True)
#         return Response(post_serializer.data)

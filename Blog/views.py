from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View, generic

from Blog.models import Posts, Tags


class MainPage(View):
    template_name = "Blog/index.html"

    def get(self, request):
        search_params = request.GET.get("search", "")
        tag_params = request.GET.get("tags", "")
        author = request.GET.get("authors", "")
        context = {
            "tags": Tags.objects.all(),
            "posts": Posts.objects.all(),
            "authors": User.objects.all().only("username"),
        }

        if tag_params:
            context["posts"] = Posts.objects.filter(tags__tag_name=tag_params)
        if author:
            context["posts"] = Posts.objects.filter(created_by__username=author)
        if search_params:
            context["posts"] = Posts.objects.filter(content__icontains=search_params)

        return render(request, self.template_name, context)


class PostDetail(View):
    template_name = "Blog/post_detail.html"

    def get(self, request, post_id):
        post = Posts.objects.get(id=post_id)
        context = {"post": post}
        return render(request, self.template_name, context)

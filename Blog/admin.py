from django.contrib import admin

from Blog.models import Posts, Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ["tag_name"]


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["title", "created_by", "created_at"]
    filter_horizontal = ["tags"]

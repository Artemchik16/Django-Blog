from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, StringRelatedField

from Blog.models import Posts, Tags


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class PostsSerializer(ModelSerializer):
    # tags = TagsSerializer(many=True)
    tags = StringRelatedField(many=True)
    created_by = UserSerializer()

    class Meta:
        model = Posts
        fields = "__all__"

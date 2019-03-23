from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email"]


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    class Meta:
        model = Post
        fields = ['id','title','content','author']
        read_only_fields = ['author']

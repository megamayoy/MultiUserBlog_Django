from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from blog.models import Post
from blog.api.serializer import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRUDAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer



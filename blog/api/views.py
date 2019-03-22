from rest_framework.generics import RetrieveUpdateDestroyAPIView
from blog.models import Post
from blog.api.serializer import PostSerializer


class PostRUDAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer



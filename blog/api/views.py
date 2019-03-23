from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from blog.models import Post
from blog.api.serializer import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRUDAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer



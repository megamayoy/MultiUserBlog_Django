from rest_framework import viewsets
from blog.models import Post
from .serializer import PostSerializer

class PostCrudAPIViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



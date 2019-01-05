from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import (ListView,DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy
# Create your views here.




class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):

    model = Post
    context_object_name = 'post'

class PostCreateView(CreateView):

    model = Post
    fields = ['title','content']
    success_url = reverse_lazy('blog:blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdatView(UpdateView):

    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):

    model = Post
    success_url = reverse_lazy('blog:blog-home')
    context_object_name = 'post'


def about(request):
    return render(request,"blog/about.html")
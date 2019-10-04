from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import (ListView,DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.


class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostsListView(ListView):

    model = Post
    context_object_name = 'posts'
    template_name = "blog/user_profile.html"

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        context['profile_owner'] = user
        context['posts'] = Post.objects.filter(author = user)
        return context


class PostDetailView(DetailView):

    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin,CreateView):

    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdatView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:blog-home')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = Post
    success_url = reverse_lazy('blog:blog-home')
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


def about(request):
    return render(request,"blog/about.html")

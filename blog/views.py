from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.views.generic import ListView
# Create your views here.




class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']



def about(request):
    return render(request,"blog/about.html")
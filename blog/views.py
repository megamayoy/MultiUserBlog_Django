from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

    return render(request,'blog/base.html')

def about(request):
    return HttpResponse("<h1>about page</h1>")
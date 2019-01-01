from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

    #return render(request,'blog/index.html')
    return HttpResponse("<h1> blog home </h1>")

def about(request):
    return HttpResponse("<h1>about page</h1>")
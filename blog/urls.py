from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [

    path('',views.home,name = 'blog-home'),
    path('about/',views.about,name = 'blog-about')

]
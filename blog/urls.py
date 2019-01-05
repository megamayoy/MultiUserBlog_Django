from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [

    path('',views.PostListView.as_view(), name = 'blog-home'),
    path('about/',views.about,name = 'blog-about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name = 'post-detail'),

]
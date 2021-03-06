from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [

    path('',views.PostListView.as_view(), name = 'blog-home'),
    path('about/',views.about,name = 'blog-about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/create/',views.PostCreateView.as_view(),name = 'post-create'),
    path('post/update/<int:pk>/',views.PostUpdatView.as_view(),name = 'post-update'),
    path('post/delete/<int:pk>/',views.PostDeleteView.as_view(),name = 'post-delete'),
    path('user_profile/<username>/',views.UserPostsListView.as_view(),name = 'user-profile-details')


]
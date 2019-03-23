from django.urls import path
from . import views

urlpatterns = [

    path('post/<int:pk>/', views.PostRUDAPIView.as_view(), name='post-rud'),
    path('post/list/',views.PostListAPIView.as_view(),name = 'post-list'),
    path('post/create/',views.PostCreateAPIView.as_view(),name = 'post-create0')

]

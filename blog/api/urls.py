from django.urls import path
from . import views

urlpatterns = [

    path('post/', views.PostRUDAPIView.as_view(), name='post-rud'),

]

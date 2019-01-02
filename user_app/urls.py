from django.urls import path
from user_app import views



app_name = 'user_app'

urlpatterns = [

    path('register/', views.register_user, name = 'user-registration'),

]
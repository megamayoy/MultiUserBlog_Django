from django.urls import path,reverse_lazy
from user_app import views
from django.contrib.auth import views as auth_views

app_name = 'user_app'

urlpatterns = [

    path('register/', views.register_user, name = 'user-registration'),
    path('login/',auth_views.LoginView.as_view(template_name = "user_app/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user_app/logout.html'),name ='logout'),
    path('profile/',views.user_profile,name = 'profile'),
    path('changeinfo/',views.change_user_profile,name = 'changeinfo'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name = 'user_app/password_change_form.html',
                                                                  success_url = reverse_lazy('user_app:logout')), name = 'password_change'),

    #if user forgets password

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = "user_app/password_reset_form.html",
                                             email_template_name = "user_app/password_reset_email.html" ), name = 'password_reset'),


    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name = "user_app/password_reset_done.html"),
                                              name = 'password_reset_done'),


    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'user_app/password_reset_confirm.html',
                                              success_url = reverse_lazy("user_app:login")), name = 'password_reset_confirm'),
    ##
]
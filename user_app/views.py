from django.shortcuts import render,redirect
from user_app.forms import RegistrationForm
from django.contrib import messages
import user_app.models as user_models
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_user(request):

    if request.method == "POST":

        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            new_user = registration_form.save()
            username = registration_form.cleaned_data.get('username')
            user_profile = user_models.UserProfile(user = new_user)
            user_profile.save()
            messages.success(request, username + " registered successfully")
            return redirect('user_app:login')
    else:

        registration_form = RegistrationForm()

    return render(request,"user_app/register.html",context = {"registration_form" : registration_form} )

@login_required
def user_profile(request):

    return render(request,"user_app/user_profile.html")


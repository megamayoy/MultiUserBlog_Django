from django.shortcuts import render,redirect
from user_app.forms import RegistrationForm,ChangeProfileForm,ChangeUserStngsForm
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


@login_required
def change_user_profile(request):


    if request.method == 'POST':

        change_userprofile_form = ChangeProfileForm(request.POST,request.FILES,instance = request.user.userprofile)
        change_userstngs_form = ChangeUserStngsForm(request.POST,instance = request.user)

        if change_userprofile_form.is_valid() and change_userstngs_form.is_valid():

            change_userprofile_form.save()
            change_userstngs_form.save()
            return redirect('user_app:profile')

    else:

        change_userprofile_form = ChangeProfileForm(instance = request.user.userprofile)
        change_userstngs_form = ChangeUserStngsForm(instance = request.user)


    return render(request,"user_app/change_user_profile.html",
                  context = { "change_userprofile_form" : change_userprofile_form , "change_userstngs_form" : change_userstngs_form})
from django.shortcuts import render,redirect
from user_app.forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def register_user(request):

    if request.method == "POST":

        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, username + " registered successfully")
            return redirect('user_app:login')
    else:

        registration_form = RegistrationForm()

    return render(request,"user_app/register.html",context = {"registration_form" : registration_form} )
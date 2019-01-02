from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register_user(request):

    if request.method == "POST":

        registration_form = UserCreationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            messages.success(request,"you registered successfully")
            return redirect('blog:blog-home')
    else:

        registration_form = UserCreationForm()

    return render(request,"user_app/register.html",context = {"registration_form" : registration_form} )
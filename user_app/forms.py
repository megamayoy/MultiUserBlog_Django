from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from user_app.models import UserProfile
from django import forms




class RegistrationForm(UserCreationForm):


    email = forms.EmailField(required=True)


    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username','email','password1' ,'password2']


class ChangeProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['profile_pic']

        labels = {

            'profile_pic' : "profile picture"
        }


class ChangeUserStngsForm(forms.ModelForm):

    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username' , 'email']





class ForgotPasswordForm(PasswordResetForm):


    def clean_email(self):

        email = self.cleaned_data['email']

        if not User.objects.filter(email__iexact= email).exists():
            raise forms.ValidationError("there's no user that uses that email")
        return email



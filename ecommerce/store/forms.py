from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField();
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        print(f"Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']} ")
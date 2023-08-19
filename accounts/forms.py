from typing import Any, Dict
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.views import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    error_css_class = 'invalid-feedback'

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username')
    
    def clean(self):
        data = self.cleaned_data
        print("Data: ", data)

        if User.objects.filter(email=data.get("email")).exists():
            self.add_error('email', f'Email {data.get("email")} already exists')

        if User.objects.filter(username=data.get("username")).exists():
            self.add_error('username', f'Username {data.get("username")} already exists')

        return super().clean()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Updating forms attributes
        for field in self.fields:
            new_data = {
                "class": 'form-control',
                "placeholder": str(field),
            }
            self.fields[str(field)].widget.attrs.update(new_data)


class UserLoginForm(AuthenticationForm):

    username = forms.EmailField(label='Email', error_messages={
                                'invalid': 'Please enter a valid email address in the format xyz@domain.com'})
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    error_css_class = 'invalid-feedback'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Updating forms attributes
        for field in self.fields:
            new_data = {
                "class": 'form-control',
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )

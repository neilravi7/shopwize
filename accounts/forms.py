from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.views import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    error_css_class = 'invalid-feedback'
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'username')

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
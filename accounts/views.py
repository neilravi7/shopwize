from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserLoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from accounts.models import Profile
from django.http import HttpResponse
from django.contrib.auth import views as auth_view
from django.contrib.messages.views import SuccessMessageMixin
from order.models import Order

# from django.core.exceptions import PermissionDenied


# Create your views here.

class UserCreationView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        # email confirmation
        user.is_active = False
        user.save()
        response =  super().form_valid(form)
        
        messages.success(
            self.request, f"Account created please verify your account! "
        )

        return response
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.error(
                    self.request, f"Already registered ! "
                )
            return redirect('shop:home')
        return super().dispatch(request, *args, **kwargs)


def user_verification(request, token):
    token = token
    try:
        profile = Profile.objects.get(email_token=token)
        profile.is_email_verified = True
        profile.email_token=None
        profile.user.is_active = True
        profile.user.save()
        profile.save()
    except Exception as e:
        return HttpResponse(f"<h1>Link is expired</h1><p>Error:{str(e)}</p>")

    messages.success(
            request, f"Account verification successfully done! "
        )
    return redirect('accounts:login')


def email_template(request):
    return render(request, 'emails/email.html')


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('shop:home')

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        next_url = self.request.GET.get('next')
        user = authenticate(self.request, email=email, password=password)
        if user:
            login(self.request, user)
            response =  super().form_valid(form)
            
            messages.success(
                    self.request, f"Login Successful ! "
                    f"Welcome {user.email}."
                )
            
            if next_url:
                return redirect(next_url)
            
            return response
        else:
            messages.error(
                    self.request, f"Invalid Credientials ! "
                )
            
            response = self.form_invalid(form)
            return response
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.error(
                    self.request, f"Already Logged in ! "
                )
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class UserLogout(SuccessMessageMixin, auth_view.LogoutView):
    success_message = "User logout successfully"

    def get_success_url(self):
        messages.success(
                    self.request, f"User logout!"
                )
        return reverse_lazy('accounts:login')

def my_account(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/my_account.html', {"orders":orders})
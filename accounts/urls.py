from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns=[
    path('register', views.UserCreationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('activate/<uuid:token>', views.user_verification, name='activate'),
    path('logout', views.UserLogout.as_view(template_name='account/login.html', next_page="accounts:login"), name='logout'),
    path('email-templates/', views.email_template, name='email'),
    path('my-account/', views.my_account, name='my_account'),
]
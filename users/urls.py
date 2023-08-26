from django.contrib.auth import views as auth_views
from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, EmailVerificationView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email_verify/<uuid:token>/', EmailVerificationView.as_view(), name='email_verify'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]

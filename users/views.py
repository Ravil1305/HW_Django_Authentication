from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User
from users.utils import send_verification_email


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def reset_password_and_send_email(self, email):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return "User with this email address is not registered"

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            subject="Восстановление пароля",
            message=f"Здравствуйте, {user.email}!\n\n Ваш новый пароль: {new_password} \n\n Используйте его для "
                    f"входа на сайт.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return "A new password has been sent to your email address."

    def post(self, request, *args, **kwargs):
        if "reset_password" in request.POST:
            email = request.POST.get("email")
            message = self.reset_password_and_send_email(email)
            return JsonResponse({"message": message}, status=200)
        else:
            return super().post(request, *args, **kwargs)


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        send_verification_email(self.request, self.object)
        return response


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verified.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, email_verification_token=self.kwargs.get('token'))
        user.email_verified = True
        user.email_verification_token = None
        user.save()
        return super().get(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

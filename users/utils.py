from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


def send_verification_email(request, user):
    verification_url = request.build_absolute_uri(
        reverse('users:email_verify', kwargs={'token': user.email_verification_token})
    )

    message = f'Для завершения регистрации в нашем сервисе, пожалуйста, перейдите по ссылке: {verification_url}'

    send_mail(
        'Подтверждение электронной почты',
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )

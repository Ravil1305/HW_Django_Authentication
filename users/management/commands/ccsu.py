from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='rafnuriev@mail.ru',
            first_name="Raf",
            last_name="Nuriev",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password("1305")
        user.save()

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_list = [
            {'name': 'Категория 4', 'description': 'Описание категории 4'},
            {'name': 'Категория 5', 'description': 'Описание категории 5'},
            {'name': 'Категория 6', 'description': 'Описание категории 6'},
            {'name': 'Категория 7', 'description': 'Описание категории 7'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)


        self.stdout.write(self.style.SUCCESS('Данные успешно загружены.'))

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from minisite.models import Category

UserModel = get_user_model()

CATEGORIES = [
    {
        'name': 'Fruit',
        'products': [
            {
                'name': 'Banane',
                'price': 1.50,
                'stock': 1000
            },
            {
                'name': 'Kiwi',
                'price': 2.50,
                'stock': 1000
            },
            {
                'name': 'Ananas',
                'price': 2.00,
                'stock': 1000
            },
        ]
    },
    {
        'name': 'Légumes',
        'products': [
            {
                'name': 'Courgette',
                'price': 3.50,
                'stock': 1000
            }
        ]
    },
    {
        'name': 'Épicerie',
        'products': [
            {
                'name': 'Sel',
                'price': 0.50,
                'stock': 1000
            }
        ]
    }
]

ADMIN_ID = 'admin-oc'
ADMIN_PASSWORD = 'password-oc'


class Command(BaseCommand):

    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Category.objects.all().delete()

        for data_category in CATEGORIES:
            category = Category.objects.create(name=data_category['name'])
            for data_product in data_category['products']:
                product = category.products.create(
                    name=data_product['name'],
                    price=data_product['price'],
                    stock=data_product['stock']
                )

        UserModel.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)

        self.stdout.write(self.style.SUCCESS("All Done !"))
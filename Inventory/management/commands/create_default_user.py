# Create directories: Inventory/management/ and Inventory/management/commands/
# Then create this file: Inventory/management/commands/create_default_user.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a default superuser'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='leonardo.byon@gmail.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Default superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Default superuser already exists'))

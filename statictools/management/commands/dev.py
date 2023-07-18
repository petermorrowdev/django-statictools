from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            call_command('runserver', use_static_handler=False)
        except TypeError:
            call_command('runserver')

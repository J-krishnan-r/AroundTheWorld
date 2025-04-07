# filepath: AroundTheWorld/management/commands/deploy.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run deployment tasks'

    def handle(self, *args, **kwargs):
        self.stdout.write("Running collectstatic...")
        call_command('collectstatic', '--noinput')

        self.stdout.write("Running makemigrations...")
        call_command('makemigrations')

        self.stdout.write("Running migrate...")
        call_command('migrate')

        self.stdout.write("Deployment tasks completed.")
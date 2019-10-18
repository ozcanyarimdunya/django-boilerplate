from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError

User = get_user_model()


class Command(BaseCommand):
    """
    Create superusers management command

    python manage.py superuser -u admin1 admin2 -p pass1 pass2 -e admin@mail1.com admin2@mail2.com
    """

    help = 'Create superusers management command'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', nargs='+', type=str)
        parser.add_argument('-p', '--password', nargs='+', type=str)
        parser.add_argument('-e', '--email', nargs='+', type=str)

    def handle(self, *args, **options):
        username = options.get('username')
        password = options.get('password')
        email = options.get('email', [])

        for u, p, e in zip(username, password, email):
            try:
                User.objects.create_superuser(username=u, password=p, email=e)
                self.stdout.write(self.style.SUCCESS(
                    'Superuser with "{}" username created!'.format(u)
                ))
            except IntegrityError:
                self.stdout.write(self.style.ERROR(
                    'Superuser with "{}" username already created!'.format(u)
                ))

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

AuthUserModel = get_user_model()


class Command(BaseCommand):
    help = 'Create profile for users without one.'

    def handle(self, *args, **options):
        users = AuthUserModel.objects.filter(profile=None)

        print(f'Updating a total of {len(users)} users.')

        for user in users:
            Profile.objects.create(
                user=user,
            )

from uuid import uuid4
import requests
from django.core.files.base import ContentFile


USER_FIELDS = ['email', 'first_name', 'last_name']


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = {name: kwargs.get(name, details.get(name))
              for name in backend.setting('USER_FIELDS', USER_FIELDS)}
    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields, is_social_user=True)
    }


def set_profile_picture(strategy, details, backend, user, is_new, *args, **kwargs):
    if is_new:
        response = kwargs.get('response')

        if response:
            profile_picture_url = None

            if backend.name == 'facebook':
                profile_picture_url = 'https://graph.facebook.com/%s/picture?access_token=%s&type=large' % (
                    response['id'],
                    response['access_token']
                )
            elif backend.name == 'google-oauth2':
                profile_picture_url = response['picture']

            if profile_picture_url:
                try:
                    profile_image_response = requests.get(profile_picture_url)
                except requests.HTTPError:
                    pass
                else:
                    profile = user.profile
                    profile.avatar.save(f'{uuid4()}.jpg', ContentFile(profile_image_response.content))

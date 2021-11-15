from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.utils import timezone
from utils.constants.activation import ACTIVATION_DICT


def get_expires_at():
    return timezone.now() + timezone.timedelta(**ACTIVATION_DICT)


class Activation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activation')
    token = models.CharField(max_length=64, null=True, default=None, blank=False, unique=True)
    expires_at = models.DateTimeField(default=get_expires_at)
    activated_at = models.DateTimeField(null=True, default=None, blank=False)

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default='users/profile_images/default_image.jpg')

    @property
    def image_url(self):
        if self.avatar:

            return self.avatar.url

        return static('users/profile_images/default_image.jpg')


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')  # user.cart - gives access to a user's cart
    data = models.JSONField()

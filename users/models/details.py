from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.utils import timezone
from utils.constants.activation import ACTIVATION_DICT


class Activation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activation')
    token = models.CharField(max_length=64, null=True, default=None, blank=False, unique=True)
    expires_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(**ACTIVATION_DICT))
    activated_at = models.DateTimeField(null=True, default=None, blank=False)


    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token

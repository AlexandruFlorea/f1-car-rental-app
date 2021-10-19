import json
import secrets
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models.details import Activation, Profile
from users.email import send_activation_email


AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    if instance.pk is None:
        instance.is_active = True
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def create_activation(instance, created, **kwargs):
    if created:
        activation = Activation(
            user=instance,
            token=secrets.token_hex(32),
        )
        activation.save()

        send_activation_email(activation)


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    if created is True:
        Profile.objects.create(user=instance)
from django.test import TestCase
from django.core import mail
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from users.models.details import Activation

AuthUserModel = get_user_model()


class IsActiveTestCase(TestCase):
    def setUp(self) -> None:
        self._user = {
            'email': 'a@gmail.com',
            'first_name': 'John',
            'last_name': 'doe',
        }

    def test_user_is_created_as_inactive(self):
        user = AuthUserModel(
            email=self._user['email'],
            first_name=self._user['first_name'],
            last_name=self._user['last_name'],
        )
        user.set_password('python123')
        user.save()

        user = AuthUserModel.objects.get(email=self._user['email'])

        self.assertEqual(user.is_active, False)
        self.assertEqual(user.password, None)


class ActivationTestCase(TestCase):
    def setUp(self) -> None:
        email = 'a@gmail.com'

        AuthUserModel.objects.create(
            email=email,
            first_name='John',
            last_name='Doe',
        )

        self._user = AuthUserModel.objects.get(email=email)
        self._activation = Activation.objects.get(user__email=self._user.email)

    def test_inactive_user_has_an_activation_relationship(self):
        self.assertNotEqual(self._activation.expires_at, None)
        self.assertNotEqual(self._activation.token, None)
        self.assertEqual(self._activation.activated_at, None)

    def test_send_activation_email(self):
        self.assertEqual(len(mail.outbox), 1)

        activation_email = mail.outbox[0]
        print('activation_email.body', activation_email.body)
        expected_content_link = f'<a href="{settings.LOCALHOST_DOMAIN}{reverse("users:activate", args=(self._activation.token, ))}">'

        self.assertEqual(activation_email.to, [self._user.email])
        self.assertIn(expected_content_link, activation_email.body)

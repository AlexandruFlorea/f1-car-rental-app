from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from utils.constants.activation import ACTIVATION_VALUE, ACTIVATION_UNIT
from django.conf import settings
from django.shortcuts import reverse


def send_activation_email(activation):
    user = activation.user
    activate_route = reverse('users:activate', args=(activation.token,))

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'unit': ACTIVATION_UNIT,
        'value': ACTIVATION_VALUE,
        'url': f'{settings.LOCALHOST_DOMAIN}{activate_route}'
    }

    template = get_template('users/email/activation.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Your account has been created!',
        body=content,
        to=[user.email],
    )
    mail.content_subtype = 'html'
    # mail.attach()
    mail.send()

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from users.email import send_activation_email
from django.utils import timezone
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html


AuthUserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = AuthUserModel
        fields = ['first_name', 'last_name', 'email']

    password1 = None
    password2 = None

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=commit)
        send_activation_email(user)

        return user


class PasswordForm(forms.Form):
    password = forms.CharField(
        max_length=128,
        required=True,
        label='Password',
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html()
    )
    password_confirmation = forms.CharField(
        max_length=128,
        required=True,
        label='Confirm password',
        widget=forms.PasswordInput
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')

        validate_password(password, user=self._user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('Password not confirmed.')

        return password_confirmation

    def save(self):
        self._user.set_password(self.cleaned_data['password'])
        self._user.is_active = True
        self._user.save()

        self._user.activation.token = None
        self._user.activation.activated_at = timezone.now()
        self._user.activation.save()

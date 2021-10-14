from django.shortcuts import render, Http404, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import RegisterForm, PasswordForm
from users.models import Activation
from users.email import send_activation_email
from django.utils import timezone
import secrets
from utils.constants.activation import ACTIVATION_DICT



def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(f'{username}')

        if user is None:
            raise Http404('Username or password not provided.')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")

    return redirect('/')


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")

            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })


def activate(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.expires_at < timezone.now():
        return redirect('users:regenerate_token', args=(token, ))

    if request.method == 'GET':
        form = PasswordForm(activation.user)
    else:
        form = PasswordForm(activation.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))

    return render(request, 'users/set_password.html', {
        'form': form,
        'token': token,
    })


def regenerate_token(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.expires_at >= timezone.now():
        redirect('users:activate', args=(token, ))

    activation.token = secrets.token_hex(32)
    activation.expires_at = timezone.now() + timezone.timedelta(**ACTIVATION_DICT)
    activation.save()

    send_activation_email(activation)

    return redirect('/')


def show_profile(request):
    pass
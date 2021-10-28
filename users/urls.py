from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import login_user, register_user, logout_user, show_profile, activate, regenerate_token, password_reset_request

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/', show_profile, name='profile'),
    path('activate/<str:token>/', activate, name='activate'),
    path('regenerate_token/<str:token>/', regenerate_token, name='regenerate_token'),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

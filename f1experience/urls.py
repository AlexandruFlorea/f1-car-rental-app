"""f1experience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from f1experience.views import homepage_view, search_site, about_page


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include('my_admin.urls')),  # my custom admin site
    path('', homepage_view, name='homepage'),
    path('search/', search_site, name='search'),
    path('cars/', include('cars.urls')),
    path('users/', include('users.urls')),
    path('tracks/', include('tracks.urls')),
    path('bookings/', include('bookings.urls')),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),  # just has to be here, for password reset to work properly
    path('about/', about_page, name='about'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

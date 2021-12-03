from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from api.register import RegisterViewSet
from api.cars import CarViewSet
from api.tracks import TrackViewSet
from api.bookings import BookingViewSet


router = DefaultRouter()  # instantiate the router
router.register(r'register', RegisterViewSet, basename='register')  # This is the register url
router.register(r'cars', CarViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),  # this includes all the urls registered in the router
    path('browser-auth/', include('rest_framework.urls')),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from bookings.models import Booking


class BookingPaginator(PageNumberPagination):
    page_size = 4
    max_page_size = 4


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        depth = 1  # goes one step further in relationships and retrieves details (ex. category)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()  # here we can limit the queryset items
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = BookingPaginator

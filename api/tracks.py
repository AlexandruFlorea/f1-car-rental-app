from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from tracks.models import Track


class TrackPaginator(PageNumberPagination):
    page_size = 4
    max_page_size = 4


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
        depth = 5  # goes one step further in relationships and retrieves details (ex. category)


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()  # here we can limit the queryset items
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = TrackPaginator

from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from cars.models import Car, Category


class CarPaginator(PageNumberPagination):
    page_size = 4
    max_page_size = 4


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        depth = 5  # goes one step further in relationships and retrieves details (ex. category)


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#         depth = 1  # goes one step further in relationships and retrieves details (ex. category)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CarPaginator

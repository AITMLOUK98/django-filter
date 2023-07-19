from rest_framework import  serializers
from django_filter.models import Book


class BookSerialzer(serializers.ModelSerializer):
    auther_name = serializers.CharField(source="auther.name")
    gener = serializers.CharField(source="get_gener_display")

    class Meta:
        model = Book
        fields = (
            'name',
            'auther_name',
            'price',
            'gener'

        )
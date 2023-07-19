import django_filters
from django_filter.models import Book


class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Book
        fields = {
            'name': ['istartswith'],  # icontains, istartswith
            'auther__name': ['icontains'],  # icontains
            # 'price': ['lt', 'gt'],  # lt, gt
            'gener': ['exact'],  # exact
        }

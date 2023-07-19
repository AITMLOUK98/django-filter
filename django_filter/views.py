from django.shortcuts import render
from django.views.generic import ListView

from django_filter.models import Book
from django_filter.filter import BookFilter

from django_filter.serializers import BookSerialzer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

def index(request):
    template_name = 'index.html'
    books_filters = BookFilter(request.GET, queryset=Book.objects.all())

    context = {
        'form': books_filters.form,
        'books': books_filters.qs
    }
    return render(request, template_name, context)


class BookListView(ListView):
    queryset = Book.objects.filter(number_in_stock__gt=0)
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = self.filterset.form
        return context


class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = BookFilter


from django.core.management.base import BaseCommand
from django_filter.models import Book, Auther


class Command(BaseCommand):
    help = "Load book data"

    def handle(self, *args, **kwargs):
        # create authors
        brahim = Auther.objects.get_or_create(name='Brahim ax')[0]
        omar = Auther.objects.get_or_create(name='omar abc')[0]
        ismail = Auther.objects.get_or_create(name='imsail bcd')[0]
        imane = Auther.objects.get_or_create(name='imane abd')[0]
        khadija = Auther.objects.get_or_create(name='khadija bnd')[0]

        # create books

        Book.objects.get_or_create(
            name='1872',
            auther=brahim,
            price=20.99,
            gener=Book.GenerChoice.SCI_FI,
            number_in_stock=4

        )
        Book.objects.get_or_create(
            name='appel',
            auther=omar,
            price=78.99,
            gener=Book.GenerChoice.NON_FICTION,
            number_in_stock=8

        )
        Book.objects.get_or_create(
            name='izjeoi',
            auther=ismail,
            price=12.99,
            gener=Book.GenerChoice.OTHER,
            number_in_stock=2

        )
        Book.objects.get_or_create(
            name='mecro',
            auther=brahim,
            price=30.99,
            gener=Book.GenerChoice.SCI_FI,
            number_in_stock=9

        )
        Book.objects.get_or_create(
            name='mercro abcd',
            auther=khadija,
            price=49.99,
            gener=Book.GenerChoice.CRIM,
            number_in_stock=3

        )
        Book.objects.get_or_create(
            name='The 100',
            auther=imane,
            price=27.99,
            gener=Book.GenerChoice.SCI_FI,
            number_in_stock=7

        )

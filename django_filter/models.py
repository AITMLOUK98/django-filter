from django.db import models

# Create your models here.

from django.db import models


class Book(models.Model):
    class GenerChoice(models.TextChoices):
        CRIM = 'C'
        NON_FICTION = 'N'
        OTHER = 'O'
        SCI_FI = 'S'
    name = models.CharField(max_length=128)
    price = models.FloatField()
    number_in_stock = models.PositiveIntegerField(default=0)
    gener = models.CharField(max_length=1, choices=GenerChoice.choices)
    auther = models.ForeignKey('Auther', on_delete=models.CASCADE)


class Auther(models.Model):
    name = models.CharField(max_length=128)

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('api/', views.BookApiView.as_view(), name='api'),
]

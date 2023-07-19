# Django Filter

Django Filter is a powerful package that simplifies the process of filtering querysets in Django. It provides a simple and intuitive way to create dynamic filters for your Django models without having to write complex SQL queries.

## Features

- Filter querysets based on specific criteria or conditions
- Supports various types of filters, including text, numbers, dates, booleans, and more
- Provides a user-friendly interface for creating and applying filters
- Enables complex filtering by combining multiple filters using logical operators (AND, OR)
- Supports integration with Django's built-in forms and templates
- Improves performance by optimizing database queries

## Installation

To install Django Filter, follow these steps:

1. Make sure you have Django installed in your project.

2. Install Django Filter using pip:

```pip install django-filter```

3. Add 'django_filters' to your Django project's `INSTALLED_APPS` setting in the settings.py file:
```python
INSTALLED_APPS = [
    ...
    'django_filters',
]

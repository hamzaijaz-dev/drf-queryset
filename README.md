Introduction
=========================
The DRF Queryset Mixin is a utility for optimizing database queries in Django REST Framework (DRF) viewsets. It provides a mixin called `QuerysetMixin` that allows you to easily optimize your queries by specifying deferred, selected related, and prefetched related fields.

Installation
------------
pip install drf-queryset

Usage
-----
Please follow the steps:

1. Import the `QuerysetMixin` from `drf_queryset.mixins`.
2. In your viewset class, inherit from `QuerysetMixin`.
3. `only_fields`: List of fields to be only fetched in the query.
4. `defer_fields`: List of fields to be deferred in the query.
5. `select_related_fields`: List of fields to be select_related in the query.
6. `prefetch_related_fields`: List of fields to be prefetch_related in the query.

Note: These fields are optional, you can use them depending upon your requirements of queryset and structure of the model fields.

Example
-------
Here's a basic example of how you can use this package in your django rest framework application:

```
from drf_queryset.mixins import QuerysetMixin
from rest_framework.viewsets import ModelViewSet
from .models import YourModel
from .serializers import YourSerializer

class MyViewSet(QuerysetMixin, ModelViewSet):
    queryset = YourModel.objects.all()  # Replace with your queryset
    serializer_class = YourSerializer  # Replace with your serializer

    defer_fields = ['field1', 'field2']  # Add your defer fields here
    only_fields = ['field3', 'field4']  # Add your only fields here
    select_related_fields = ['related_field1', 'related_field2']  # Add your select_related fields here
    prefetch_related_fields = ['m2m_field', 'reverse_fk_field']  # Add your prefetch_related fields here
```

License
-------
MIT License
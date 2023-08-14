class QuerysetMixin:

    def __init__(self):
        self.defer_fields = None
        self.only_fields = None

    def get_queryset(self):
        queryset = super().get_queryset()

        optimization_fields = self.defer_fields or self.only_fields
        if optimization_fields:
            if self.defer_fields:
                queryset = queryset.defer(*self.defer_fields)
            else:
                queryset = queryset.only(*self.only_fields)

        queryset = self.check_related_fields(queryset)

        return queryset

    def check_related_fields(self, queryset):

        if hasattr(self, 'select_related_fields'):
            queryset = queryset.select_related(*self.select_related_fields)

        if hasattr(self, 'prefetch_related_fields'):
            queryset = queryset.prefetch_related(*self.prefetch_related_fields)

        return queryset


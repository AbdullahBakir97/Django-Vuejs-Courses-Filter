from django_filters import rest_framework as filters


class CourseFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='Category', method='filter_by_category')
    
    def filter_by_category(self, queryset, name, value):
        ids = value.split(',')
        return queryset.filter(category__id__in=ids)
    
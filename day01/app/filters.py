import django_filters
import django_filters.filterset
from .models import Category, Item

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = '__all__'


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['name', 'category', 'unit']

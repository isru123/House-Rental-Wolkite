import django_filters

from .models import Listing,RentalConditions

class ListingFilter(django_filters.FilterSet):
    available_start = django_filters.CharFilter(lookup_expr='exact')
    address = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Listing
        fields = {'available_start': {'exact'}, 'address':{'icontains'}}
        
import django_filters

from .models import Listing

class ListingFilter(django_filters.FilterSet):
    
    class Meta:
        model = Listing
        fields = {'price': {'exact'}, 'house_kind':{'icontains'}}
        
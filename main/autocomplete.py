from dal import autocomplete
from .models import AddressOfListing
from django.http import HttpResponse
import json


class AddressAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = AddressOfListing.objects.all()

        if self.q:
            qs = qs.filter(Address__istartswith=self.q)

        return qs
    
    
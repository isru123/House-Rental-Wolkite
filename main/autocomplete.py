# from dal import autocomplete
# from .models import AddressOfListing
# from django.http import HttpResponse
# import json


# class AddressAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = AddressOfListing.objects.all()

#         if self.q:
#             qs = qs.filter(Address__istartswith=self.q)

#         return qs
    
<<<<<<< HEAD
    
#     # def get(self, request, *args, **kwargs):
#     #     if request.is_ajax():
#     #         self.q = request.GET.get('term', '')
#     #         context = self.get_context_data()
#     #         queryset = self.get_queryset()
#     #         suggestions = [str(item) for item in queryset]
#     #         response_data = json.dumps(suggestions)
#     #         return HttpResponse(response_data, content_type='application/json')
#     #     return super().get(request, *args, **kwargs)
=======
    
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

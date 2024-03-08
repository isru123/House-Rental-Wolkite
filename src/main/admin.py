from django.contrib import admin

from .models import Listing, ListingSpaceOverview

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    
class ListingSpaceOverviewAdmin(admin.ModelAdmin):
    pass
      

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingSpaceOverview, ListingSpaceOverviewAdmin)



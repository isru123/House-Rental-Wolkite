from django.contrib import admin

from .models import Listing, ListingSpaceOverview, ListingHouseArea, ListingHouseAmenities, RentalConditions, RulesAndPreferences

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    
class ListingSpaceOverviewAdmin(admin.ModelAdmin):
    pass
      

class ListingHouseAreaAdmin(admin.ModelAdmin):
    pass


class ListingHouseAmenitiesAdmin(admin.ModelAdmin):
    pass


class RentalConditionsAdmin(admin.ModelAdmin):
    pass

class RulesAndPreferencesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingSpaceOverview, ListingSpaceOverviewAdmin)
admin.site.register(ListingHouseArea, ListingHouseAreaAdmin)
admin.site.register(ListingHouseAmenities, ListingHouseAmenitiesAdmin)
admin.site.register(RentalConditions, RentalConditionsAdmin)
admin.site.register(RulesAndPreferences, RulesAndPreferencesAdmin)
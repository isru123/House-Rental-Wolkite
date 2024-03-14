from django.contrib import admin

from .models import Listing,LikedListing, Review, Booking,ListingSpaceOverview, ListingHouseArea, ListingHouseAmenities, RentalConditions, RulesAndPreferences

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

class LikedListingAdmin(admin.ModelAdmin):
    pass

class AmenityAdmin(admin.ModelAdmin):
    pass

class ListingSpaceAdmin(admin.ModelAdmin):
    pass

class HouseAreaAdmin(admin.ModelAdmin):
    pass

class RentalConditionAdmin(admin.ModelAdmin):
    pass

class RulesAdmin(admin.ModelAdmin):
    pass



# class ImageAdmin(admin.ModelAdmin):
#     pass

# class BookingAdmin(admin.ModelAdmin):
#     pass

# class RoomBookingAdmin(admin.ModelAdmin):
#     pass

class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingSpaceOverview, ListingSpaceOverviewAdmin)
admin.site.register(ListingHouseArea, ListingHouseAreaAdmin)
admin.site.register(ListingHouseAmenities, ListingHouseAmenitiesAdmin)
admin.site.register(RentalConditions, RentalConditionsAdmin)
admin.site.register(RulesAndPreferences, RulesAndPreferencesAdmin)
admin.site.register(LikedListing, LikedListingAdmin)
# admin.site.register(Amenity, AmenityAdmin)
# admin.site.register(ListingSpace, ListingSpaceAdmin)
# admin.site.register(HouseArea, HouseAreaAdmin)
# admin.site.register(RentalCondition, RentalConditionAdmin)
# admin.site.register(Rules, RulesAdmin)

# admin.site.register(Image,ImageAdmin)
# admin.site.register(Booking, BookingAdmin)
admin.site.register(Review,ReviewAdmin)




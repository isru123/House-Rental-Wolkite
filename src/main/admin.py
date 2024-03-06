from django.contrib import admin

from .models import Listing, Review, RoomBooking, Booking, Image, ListingSpaceOverview, Room, ListingHouseArea, ListingHouseAmenities, RentalConditions, RulesAndPreferences

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

class RoomAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

class BookingAdmin(admin.ModelAdmin):
    pass

class RoomBookingAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingSpaceOverview, ListingSpaceOverviewAdmin)
admin.site.register(ListingHouseArea, ListingHouseAreaAdmin)
admin.site.register(ListingHouseAmenities, ListingHouseAmenitiesAdmin)
admin.site.register(RentalConditions, RentalConditionsAdmin)
admin.site.register(RulesAndPreferences, RulesAndPreferencesAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(RoomBooking, RoomBookingAdmin)
admin.site.register(Review,ReviewAdmin)





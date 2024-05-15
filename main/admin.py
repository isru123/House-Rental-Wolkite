from django.contrib import admin

<<<<<<< HEAD
from .models import Listing,LikedListing,Image,ListingSpaceOverview, ListingHouseArea,Upload, ListingHouseAmenities, RentalConditions, RulesAndPreferences,Review,AddressOfListing
=======
from .models import Listing,LikedListing,Image,ListingSpaceOverview, ListingHouseArea,Document, ListingHouseAmenities, RentalConditions, RulesAndPreferences,Review,AddressOfListing,Upload
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

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



class ImageAdmin(admin.ModelAdmin):
    pass



class BookingAdmin(admin.ModelAdmin):
    pass



class ReviewAdmin(admin.ModelAdmin):
    
    pass

class AddressOfListingAdmin(admin.ModelAdmin):
    
    pass


class DocumentAdmin(admin.ModelAdmin):
    pass

class UploadAdmin(admin.ModelAdmin):
    pass





admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingSpaceOverview, ListingSpaceOverviewAdmin)
admin.site.register(ListingHouseArea, ListingHouseAreaAdmin)
admin.site.register(ListingHouseAmenities, ListingHouseAmenitiesAdmin)
admin.site.register(RentalConditions, RentalConditionsAdmin)
admin.site.register(RulesAndPreferences, RulesAndPreferencesAdmin)


admin.site.register(Image,ImageAdmin)
admin.site.register(AddressOfListing,AddressOfListingAdmin)
<<<<<<< HEAD
# admin.site.register(Document,DocumentAdmin)
# admin.site.register(Booking, BookingAdmin)
=======
admin.site.register(Document,DocumentAdmin)
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9


admin.site.register(Upload,UploadAdmin)







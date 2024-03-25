from django.contrib import admin

from .models import Profile, Location,OTP


class LocationAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    list_display=['id','user']
    
    
class OTPAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile,UserAdmin)
admin.site.register(OTP,OTPAdmin)
admin.site.register(Location, LocationAdmin)



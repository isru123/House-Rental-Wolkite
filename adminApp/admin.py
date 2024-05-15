from django.contrib import admin

# Register your models here.


from .models import Message

class ConversationAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass




admin.site.register(Message,MessageAdmin)


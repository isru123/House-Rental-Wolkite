from django.contrib.auth.models import User
from django.db import models

from main.models import Listing

class Conversation(models.Model):
    list = models.ForeignKey(Listing, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)













# from django.db import models

# from users.models import Profile

# class Message(models.Model):
#     body = models.TextField()
#     sent_by = models.CharField(max_length=255)
#     created_at  = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    
    
#     class Meta:
#         ordering = ('created_at',)
        
    
#     def __str__(self):
#         return f"{self.sent_by}"
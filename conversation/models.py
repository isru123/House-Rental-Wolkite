from django.db import models

from users.models import UserProfile

class Message(models.Model):
    body = models.TextField()
    sent_by = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.SET_NULL)
    
    
    class Meta:
        ordering = ('created_at',)
        
    
    def __str__(self):
        return f"{self.sent_by}"
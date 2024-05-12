# from django.contrib.auth.models import User
# from django.db import models

# from main.models import Listing

# class Conversation(models.Model):
#     item = models.ForeignKey(Listing, related_name='conversations', on_delete=models.CASCADE)
#     members = models.ManyToManyField(User, related_name='conversations')
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('-modified_at',)
    
# class ConversationMessage(models.Model):
#     conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
#     recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, null=True)
# models.py
from main.models import Listing

from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    item = models.ForeignKey(Listing, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    has_new_messages = models.BooleanField(default=False)  # New field to indicate if there are new messages
    seen = models.BooleanField(default=False)  # New field to indicate if the user has seen or clicked on the conversation

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        # Update the has_new_messages attribute of the conversation when a new message is received
        self.conversation.has_new_messages = True
        self.conversation.save()
        super().save(*args, **kwargs)

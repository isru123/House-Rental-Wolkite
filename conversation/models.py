# from django.contrib.auth.models import User
# from django.db import models

# from main.models import Listing

# class Conversation(models.Model):
#     listing = models.ForeignKey(Listing, related_name='conversations', on_delete=models.CASCADE)
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

#     class Meta:
#         ordering = ('created_at',)

# from django.shortcuts import render

# # Create your views here.

# def message_view(request):
#     return render(request, 'conversation/message.html')


from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    room = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
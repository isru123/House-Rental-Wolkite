from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Listing
from django.urls import reverse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .forms import ConversationMessageForm
from .models import ConversationMessage
from .forms import ConversationMessageForm
from .models import Conversation

@login_required



def new_conversation(request, id):
    listing = get_object_or_404(Listing, id=id)

    # Check if the current user is the owner of the listing
    if request.user.profile.userType == "Owner" and listing.seller.user == request.user:
        return redirect('main:home')

    # Check if there are existing conversations related to the listing for the current user
    conversations = Conversation.objects.filter(item=listing, members=request.user)
    if conversations.exists():
        return redirect('detail', conversation_id=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # Create a new conversation
            conversation = Conversation.objects.create(item=listing)
            conversation.members.add(request.user, listing.seller.user)
            conversation.save()

            # Create a new conversation message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('detail', conversation_id=conversation.id)
    else:
        form = ConversationMessageForm()

    context = {
        'form': form,
        'listing': listing
    }
    return render(request, 'conversation/new.html', context)


from .models import Conversation

from .models import Conversation

def inbox(request, conversation_id):
    profile = request.user.profile
    conversations = Conversation.objects.filter(item__seller=profile)
    context = {
        'conversations': conversations
    }
    return render(request, 'conversation/inbox.html', context)



# def detail(request, conversation_id):
#     conversation = get_object_or_404(Conversation, id=conversation_id, members=request.user)

#     if request.method == 'POST':
#         form = ConversationMessageForm(request.POST)

#         if form.is_valid():
#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()

#             return redirect('detail', conversation_id=conversation_id)
#     else:
#         form = ConversationMessageForm()
#         context = {
#           'conversation': conversation,
#         'form': form}
#     return render(request, 'conversation/conversationpage.html', context)

# def detail(request, conversation_id):
#     conversation = get_object_or_404(Conversation, id=conversation_id, members=request.user)

#     if request.method == 'POST':
#         form = ConversationMessageForm(request.POST)

#         if form.is_valid():
#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()

#             # Send the new message to the WebSocket consumer
#             channel_layer = get_channel_layer()
#             async_to_sync(channel_layer.group_send)(
#                 f"conversation_{conversation_id}",
#                 {
#                     "type": "chat_message",
#                     "message": {
#                         "username": conversation_message.created_by.username,
#                         "content": conversation_message.content,
#                         "created_at": conversation_message.created_at.strftime("%Y-%m-%d %H:%M:%S")
#                     }
#                 }
#             )

#             return redirect('detail', conversation_id=conversation_id)
#     else:
#         form = ConversationMessageForm()
#         context = {
#             'conversation': conversation,
#             'form': form
#         }
#     return render(request, 'conversation/conversationpage.html', context)



def detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, members=request.user)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('detail', conversation_id=conversation_id)
    else:
        form = ConversationMessageForm()
    context = {'conversation': conversation, 'form': form}
    return render(request, 'conversation/conversationpage.html', context)

def edit_message(request, message_id):
    if request.method == 'POST':
        new_content = request.POST.get('new_content')
        if new_content is not None:  # Check if new content is not None
            message = get_object_or_404(ConversationMessage, pk=message_id)
            message.content = new_content
            message.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'New content is empty'}, status=400)
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def delete_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(ConversationMessage, pk=message_id)
        message.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def delete_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(ConversationMessage, pk=message_id)
        message.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

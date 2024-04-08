from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Listing

from .forms import ConversationMessageForm
from .models import Conversation

@login_required



def new_conversation(request, product_id):
    listing = get_object_or_404(Listing, id=product_id)

    if request.user == listing.seller:
        return redirect('main:home')

    conversations = Conversation.objects.filter(item=listing).filter(members__in=[request.user.id])

    if conversations:
        return redirect('detail', conversation_id=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=listing)
            conversation.members.add(request.user)
            conversation.members.add(listing.seller.user)  # Access the User instance through the profile
            conversation.save()

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

def inbox(request, conversation_id):
    # Your code here
    conversations = Conversation.objects.filter(members=request.user)
    conversations = {
        'conversations': conversations
    }
    return render(request, 'conversation/inbox.html', conversations)

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
        context = {
          'conversation': conversation,
        'form': form}
    return render(request, 'conversation/conversationpage.html', context)
# # from django.shortcuts import render

# # # Create your views here.

# # def message_view(request):
# #     return render(request, 'conversation/message.html')

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, get_object_or_404, redirect
# from main.models import Listing


# from .forms import ConversationMessageForm
# from .models import Conversation

# @login_required
# def new_conversation(request, list_pk):
#     list = get_object_or_404(Listing, pk=list_pk)

#     if list.created_by == request.user:
#         return redirect('main:home')
    
#     conversations = Conversation.objects.filter(list=list).filter(members__in=[request.user.id])

#     if conversations:
#         return redirect('conversation:detail', pk=conversations.first().id)

#     if request.method == 'POST':
#         form = ConversationMessageForm(request.POST)

#         if form.is_valid():
#             conversation = Conversation.objects.create(list=list)
#             conversation.members.add(request.user)
#             conversation.members.add(list.created_by)
#             conversation.save()

#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()

#             return redirect('main:detail_product_view', pk=list_pk)
#     else:
#         form = ConversationMessageForm()
    
#     return render(request, 'conversation/new.html', {
#         'form': form
#     })

# def inbox(request):
#     conversations = Conversation.objects.filter(members__in=[request.user.id])

#     return render(request, 'conversation/inbox.html', {
#         'conversations': conversations
#     })

# @login_required
# def detail(request, pk):
#     conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

#     if request.method == 'POST':
#         form = ConversationMessageForm(request.POST)

#         if form.is_valid():
#             conversation_message = form.save(commit=False)
#             conversation_message.conversation = conversation
#             conversation_message.created_by = request.user
#             conversation_message.save()

#             conversation.save()

#             return redirect('conversation:detail', pk=pk)
#     else:
#         form = ConversationMessageForm()

#     return render(request, 'conversation/detail.html', {
#         'conversation': conversation,
#         'form': form
#     })


from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'conversation/hoom.html')


def room(request, room):
    username = request.GET.get('username') # henry
    room_details = Room.objects.get(name=room)
    return render(request, 'conversation/room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Hi, Message Sent Successfully!!")

def getMessages(request,  room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
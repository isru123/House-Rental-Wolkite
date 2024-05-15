from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from users.models import Profile,Location

from main.models import Listing,Upload
from django.urls import reverse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .forms import ConversationMessageForm
from .models import ConversationMessage
from .forms import ConversationMessageForm
from .models import Conversation
from .models import ConversationMessage
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def is_request_valid(move_in_date, move_out_date, available_start):
    move_in_date = datetime.strptime(move_in_date, '%Y-%m-%d').date() if isinstance(move_in_date, str) else move_in_date
    move_out_date = datetime.strptime(move_out_date, '%Y-%m-%d').date() if isinstance(move_out_date, str) else move_out_date
    available_start = datetime.strptime(available_start, '%Y-%m-%d').date() if isinstance(available_start, str) else available_start

    if available_start <= move_in_date <= move_out_date:
        return True
    return False




@login_required
def new_conversation(request, product_id):

    listing = get_object_or_404(Listing, id=product_id)
    
    
    
    if request.user == listing.seller:
        return redirect('main:home')

    # Check if there are existing conversations related to the listing for the current user
    conversations = Conversation.objects.filter(item=listing, members=request.user)
    if conversations.exists():
        return redirect('message:detail', conversation_id=conversations.first().id)

 
    tenant_photo_url = ''

    # Fetch tenant's document and photo
    tenant_uploads = Upload.objects.filter(tenant=request.user.profile)

    # Assuming you want to use the first upload found
    if tenant_uploads.exists():
        tenant_upload = tenant_uploads.first()
        tenant_photo_url = tenant_upload.photo.url

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

            return redirect('message:detail', conversation_id=conversation.id)
    else:
        form = ConversationMessageForm()

    context = {
        'form': form,
        'listing': listing,
     
        'tenant_photo_url': tenant_photo_url,
    }
    return render(request, 'conversation/new.html', context)





def send_notification_to_seller(seller):
    from django.core.mail import EmailMessage

    subject = "New Request for Your Listing"
    message = f"Hello {seller.user.username},\n\nYou have received a new request for your listing.\n\nPlease check your account for further details."
    email = EmailMessage(subject, message, to=[seller.email])
    email.send()



def send_notification_to_admins():
    from django.core.mail import EmailMessage
    from django.contrib.auth.models import User

    admins = User.objects.filter(is_superuser=True)

    subject = "New Request Received"
    message = "Hello Admins,\n\nA new request has been received.\n\nPlease check the system for further details."
    email = EmailMessage(subject, message, to=[admin.email for admin in admins])
    email.send()







def inbox_view(request):
    profile = request.user.profile
    conversations = Conversation.objects.filter(item__seller=profile)
    context = {
        'conversations': conversations
    }
    return render(request, 'conversation/inbox.html', context)







def detail(request, conversation_id):
  
    conversation = get_object_or_404(Conversation, id=conversation_id, members=request.user)
    listing_seller = conversation.item.seller
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            
           
                
            return redirect('message:detail', conversation_id=conversation_id)
    else:
        form = ConversationMessageForm()
    context = {'conversation': conversation, 'form': form, 'listing_seller':listing_seller}
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


def booking_page(request, conversation_id):
    # Your view logic here
    return redirect('booking_page', conversation_id=conversation_id)


@login_required
def dashboard_view(request):
    user = request.user.id
    bookings = Booking.objects.filter(tenant=request.user)
    payment_history = Payment.objects.filter(payer=request.user)
<<<<<<< HEAD
    messages_received = ConversationMessage.objects.all()
    all_payments = Payment.objects.filter(payer=request.user) | Payment.objects.filter(recipient=request.user)
    all_bookings = Booking.objects.filter(tenant=request.user)
=======
    messages_received = ConversationMessage.objects.filter(recipient=user)
    
>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9
    # Calculate the total number of messages
    
    total_messages_count = messages_received.count()
    context = {
        'all_bookings': all_bookings,
        'all_payments': all_payments,
        'bookings': bookings,
        'payment_history': payment_history,
        'messages_received': messages_received,
        'total_messages_count': total_messages_count,

    }
    return render(request, 'renterApp/dashboard.html', context)



@login_required
# def messages(request):
#     if not request.user.is_authenticated:
#         return redirect('login')

#     # Retrieve conversations where the logged-in user is a member
#     user = request.user
#     conversations = Conversation.objects.filter(members=user)

#     # Pass the conversations to the template
#     return render(request, 'renterApp/messages.html', {'conversations': conversations, 'user': user})



# Other views...

def messages(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Retrieve conversations where the logged-in user is a member
    user = request.user
    conversations = Conversation.objects.filter(members=user)

    # Pass the conversations to the template
    return render(request, 'renterApp/messages.html', {'conversations': conversations, 'user': user})

from django.http import JsonResponse

def update_seen(request, conversation_id):
    if request.method == 'POST':
        conversation = get_object_or_404(Conversation, pk=conversation_id)
        conversation.seen = True
        conversation.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})




from paymnet.models import Booking


def books(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Filter bookings where the logged-in user is either the tenant or the owner
    all_bookings = Booking.objects.filter(tenant=request.user)
    if request.method == "POST":
        search = request.POST.get("search")
        all_bookings = Booking.objects.filter(guest__user__username=search)
   
            
    page = request.GET.get('page', 1)

    paginator = Paginator(all_bookings, 7)
    try:
        all_bookings = paginator.page(page)
    except PageNotAnInteger:
        all_bookings = paginator.page(1)
    except EmptyPage:
        all_bookings = paginator.page(paginator.num_pages)
        
    context = {
        'all_bookings': all_bookings,
        
    }

    return render(request, 'renterApp/books.html', context)



def listigs(request): 
    if not request.user.is_authenticated:
        return redirect('login')
    total_verified_owner = Profile.objects.filter(userType="Public", verified=True).count()
    total_unverified_owner = Profile.objects.filter(userType="Owner", verified=False).count()

    total_verified_admin = Profile.objects.filter(userType="Admin", verified=True).count()
    total_unverified_admin = Profile.objects.filter(userType="Admin", verified=False).count()

    Dict = {
        "total_verified_owner":total_verified_owner,
        "total_unverified_owner":total_unverified_owner,
        "total_verified_admin":total_verified_admin,
        "total_unverified_admin":total_unverified_admin,
        }
    return render(request, 'renterApp/listing.html',Dict)



from django.shortcuts import render, redirect
from paymnet.models import Payment




def payments(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
<<<<<<< HEAD
    all_payments = Payment.objects.filter(payer=request.user) | Payment.objects.filter(recipient=request.user)
    all_bookings = Booking.objects.filter(tenant=request.user)

    context = {
        'all_payments': all_payments,
        'all_bookings': all_bookings
    }

    return render(request, 'renterApp/payment.html', context)
=======
    # Filter payments where the logged-in user is either the payer or the recipient
    A = Payment.objects.filter(payer=request.user) | Payment.objects.filter(recipient=request.user)
    
    page = request.GET.get('page', 1)

    paginator = Paginator(A, 7)
    try:
        A = paginator.page(page)
    except PageNotAnInteger:
        A = paginator.page(1)
    except EmptyPage:
        A = paginator.page(paginator.num_pages)
    # Pass the filtered payments to the template
  
    return render(request, 'renterApp/payment.html', {'payments':A})


def booking_ask(request):
    profile = request.user.profile
    R = Upload.objects.filter(tenant=profile)
    if request.method == "POST":
        search = request.POST.get("search")
        R = Upload.objects.filter(listing__price=search)
        
    for ask in R:
        if ask.status != 'Accepted' and ask.status != 'Rejected':
            ask.status = "Pending"
        elif ask.status == 'Accepted':
            ask.status = "Accepted"
        elif ask.status == 'Rejected':
            ask.status = "Rejected"
            
    page = request.GET.get('page', 1)

    paginator = Paginator(R, 7)
    try:
        R = paginator.page(page)
    except PageNotAnInteger:
        R = paginator.page(1)
    except EmptyPage:
        R = paginator.page(paginator.num_pages)

    return render(request,'renterApp/booking_ask.html', {'requests': R})


>>>>>>> 584c1c0a1651ba0eb4c5312543af28bafa21fef9

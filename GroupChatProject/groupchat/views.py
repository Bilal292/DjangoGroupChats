from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . models import Chat, Messages

@login_required
def chats(request):
    groupChats = Chat.objects.all()
    return render(request, 'groupchat/chats.html', {'groupChats': groupChats})

@login_required
def startChat(request,slug):
    groupChat = Chat.objects.get(slug=slug)
    messages = Messages.objects.filter(chat=groupChat)[0:25]
    return render(request, 'groupchat/startChat.html', {'groupChat': groupChat, 'messages': messages})

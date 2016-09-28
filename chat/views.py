from datetime import datetime

from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render

from .models import ChatMessage


class ChatView(View):
    def get(self, request, *args, **kwargs):
        print 'Accessed HTTP View'

        if self.request.GET.get('clear_chat_history'):
            ChatMessage.objects.all().delete()

        template_name = 'chat/chat.html'
        context = {}
        context['users'] = User.objects.all()
        context['chat_messages'] = ChatMessage.objects.all()
        context['now'] = datetime.now()
        return render(request, template_name, context)

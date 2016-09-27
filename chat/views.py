from django.views import View
from django.shortcuts import render


class ChatView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'chat/chat.html'
        return render(request, template_name)

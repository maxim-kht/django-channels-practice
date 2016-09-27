from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


class ChatView(View):
    def get(self, request, *args, **kwargs):
        # return HttpResponse('Hello Chat View!')
        template_name = 'chat/chat.html'
        return render(request, template_name)

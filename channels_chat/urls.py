from django.conf.urls import url
from django.contrib import admin
from chat.views import ChatView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ChatView.as_view(), name='chat_view')
]

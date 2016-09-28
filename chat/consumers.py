from django.contrib.auth.models import User

from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from .models import ChatMessage


@channel_session_user_from_http
def ws_connect(message):
    room = message.content['path'].replace('/', '')
    Group("chat-%s" % room).add(message.reply_channel)


@channel_session_user
def ws_receive(message):
    print 'Connected to websocket.receive'
    room = message.content['path'].replace('/', '')

    ChatMessage.objects.create(
        room=room,
        message=message['text'],
        user=User.objects.get(username=message.user.username)
    )

    Group("chat-%s" % room).send({
        "text": '%s:%s' % (message.user.username, message['text']),
    })


@channel_session_user
def ws_disconnect(message):
    print 'Connected to websocket.disconnect'
    room = message.content['path'].replace('/', '')
    Group("chat-%s" % room).discard(message.reply_channel)

import json

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session


# def http_consumer(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse(json.dumps(message.content))
#     print 'message content:'
#     for i in message.content.items(): print i
#     # Encode that resposne into message format
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)


# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data
#     message.reply_channel.send({
#         'text': message.content['text'],
#     })


# Connected to websocket.connect
def ws_add(message):
    print 'ws_add'
    print message.reply_channel
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip('/')
    Group('chat').add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    print 'ws_message'
    print message.content
    Group('chat').send({
        'text': '[user] %s' % message.content['text'],
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    print 'ws_disconnect'
    Group('chat').discard(message.reply_channel)

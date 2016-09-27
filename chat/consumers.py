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
@channel_session
def ws_connect(message):
    print 'ws_connect'
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip('/')
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group('chat-%s' % room).add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    print 'ws_message'
    print message.content
    room = message.channel_session['room']
    Group('chat-%s' % room).send({
        'text': '[user] %s' % message.content['text'],
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    print 'ws_disconnect'
    Group('chat-%s' % message.channel_session['room']).discard(message.reply_channel)

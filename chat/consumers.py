from channels import Group
from channels.sessions import channel_session


@channel_session
def ws_connect(message):
    print 'ws_connect'
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip('/')
    if not room:
        room = 'default_room'
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group('chat-%s' % room).add(message.reply_channel)


@channel_session
def ws_message(message):
    print 'ws_message'
    print message.content
    room = message.channel_session['room']
    Group('chat-%s' % room).send({
        'text': '[user] %s' % message['text'],
    })


@channel_session
def ws_disconnect(message):
    print 'ws_disconnect'
    Group('chat-%s' % message.channel_session['room']).discard(message.reply_channel)

from django.http import HttpResponse
from channels.handler import AsgiHandler
import json


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse(json.dumps(message.content))
    print 'message content:'
    for i in message.content.items(): print i
    # Encode that resposne into message format
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)

import asyncio

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse
from channels.generic.websocket import AsyncWebsocketConsumer


import json


@csrf_exempt
def webhook(request):
    """
    Webhook API for storing mandill events
    """
    if request.method == 'POST':
        event_data = json.loads(request.body.decode('utf-8'))
        # Each OPEN event will be stored in cache (Redis cache)
        cache.set(event_data['id'], json.dumps(event_data))
        return HttpResponse(status=200)
    else:
        # Only accepts POST method
        return HttpResponse(status=405)


def websocket_view(request):
    """ View for rendering template with socket connection and events notifications"""
    return render(request, 'mandrill_events.html')


class MandrillEventsConsumer(AsyncWebsocketConsumer):
    """ Websocket for sending events from mandrill to template.
        - Checks every 5 seconds in cache for new events and send it, the cache will be cleared then.
        - cache_id is the message_id, needed to fetch exact events for a message
    """
    async def connect(self):
        await self.accept()

        while True:
            # ToDo get message_id/ids
            # This is sample id
            cache_id = "111"
            data = cache.get(cache_id)
            if data:
                message = json.dumps({'event_data': data})
                await self.send(text_data=message)
                cache.delete(cache_id)
            await asyncio.sleep(5)


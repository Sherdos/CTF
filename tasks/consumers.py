import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CtfConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.ctf_id = self.scope['url_route']['kwargs']['ctf_id']
        self.ctf_group_name = f'ctf_{self.ctf_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.ctf_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.ctf_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.ctf_group_name,
            {
                'type': 'ctf_message',
                'message': data['message'],
            }
        )

    # Receive message from room group
    async def ctf_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
        }))

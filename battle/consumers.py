import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class BattleConsumer(WebsocketConsumer):
    def connect(self):
        room_name = self.scope['url_route']['kwargs']['code']

        async_to_sync(self.channel_layer.group_add)(
            'chat',
            room_name,
        )

        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat.message",
                "text": text_data,
            },
        )


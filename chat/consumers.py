import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    """потребитель вебсокета"""

    async def connect(self):
        self.user = self.scope["user"]
        self.id = self.scope["url_route"]["kwargs"]["course_id"]
        self.room_group_name = f"chat_{self.id}"

        await self.channel_layer.group_add(  # подключиться к комнате чата
            self.room_group_name, self.channel_name
        )

        await self.accept()  # принять соединение

    async def disconnect(self, close_code):
        """закрыть соединение"""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """получить сообщение из вебсокета"""
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        now = timezone.now()

        await self.channel_layer.group_send(        # отправить сообщение в комнату
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": self.user.username,
                "datetime": now.isoformat(),
            },
        )

    async def chat_message(self, event):
        """отправка сообщения в вебсокет"""
        await self.send(text_data=json.dumps(event))

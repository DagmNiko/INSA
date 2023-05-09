import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from core.models import *
from accounts.models import *




class BlogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"].email
        print(self.user)
        self.room_name = self.scope["url_route"]['kwargs']['blog_id']
        print(self.scope["url_route"])
        self.room_group_name = f'comment_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        print('connection accepted!')

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        blog = self.room_name
        content = text_data_json["content"]
        author = self.user

        comment = text_data_json["comment"]
        if comment == '':
            await self.save_new_blog(blog,content, author)
        else:
            await self.save_new_reply(comment, content, author)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "blog_fields", "blog": blog,"author": author, "content": content, "comment": comment}
        )
        # print(f'Received message from {self.channel_name}: {message}')

    # Receive message from room group
    async def blog_fields(self, event):
        blog = event["blog"]

        # tags = event["tags"]
        author = self.user
        content = event["content"]
        comment = event["comment"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"blog": blog, "author": author, "content": content, 'comment': comment}))
        
    @database_sync_to_async
    def add_blog(self, blog,content, author):
        account = Account.objects.get(email=author)
        blog = Blog.objects.get(pk=blog)

        return Comment.objects.create(author=account,blog=blog,content=content)
        
    async def save_new_blog(self, blog, content, author):
        await self.add_blog(blog, content, author)
    
    @database_sync_to_async
    def add_reply(self, comment, content, author):
        account = Account.objects.get(email=author)
        comment = Comment.objects.get(pk=comment)

        return Replies.objects.create(author=account,comment=comment,content=content)
    async def save_new_reply(self, comment, content, author):
        await self.add_reply(comment, content, author)
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from core.models import *
from accounts.models import *




class BlogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"].email
        self.userId = self.scope['user'].pk
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
        like = text_data_json["likes"]
        # selected = text_data_json["selected"]
        # count = text_data_json["count"]

        comment = text_data_json["comment"]
        if like == 'comment':
            await self.save_new_blog(blog,content, author)
        if like == 'post':
            await self.save_like(self.userId)
        if like == 'reply':
            await self.save_new_reply(comment, content, author)
        if like == 'liked':
            await self.discard_like(self.userId)
        
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "blog_fields", "blog": blog,"author": author, "content": content, "comment": comment, "likes":like}
        )
        # print(f'Received message from {self.channel_name}: {message}')

    # Receive message from room group
    async def blog_fields(self, event):
        like = event['likes']
        blog = event["blog"]

        # tags = event["tags"]
        author = self.user
        content = event["content"]
        comment = event["comment"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"blog": blog, "author": author, "content": content, 'comment': comment, 'likes': like}))
        
    @database_sync_to_async
    def add_blog(self, blog,content, author):
        account = Account.objects.get(email=author)
        blog = Blog.objects.get(pk=blog)

        return Comment.objects.create(author=account,blog=blog,content=content)
        
    async def save_new_blog(self, blog, content, author):
        await self.add_blog(blog, content, author)
    
    @database_sync_to_async
    def add_like(self, usr):
        news = Blog.objects.get(pk=self.room_name)
        
        return news.likes.add(usr)
    async def save_like(self,usr):
        await self.add_like(usr)
    
    @database_sync_to_async
    def remove_like(self, usr):
        news = Blog.objects.get(pk=self.room_name)
        
        return news.likes.remove(usr)
    async def discard_like(self,usr):
        await self.remove_like(usr)
    @database_sync_to_async
    def add_reply(self, comment, content, author):
        account = Account.objects.get(email=author)
        comment = Comment.objects.get(pk=comment)

        return Replies.objects.create(author=account,comment=comment,content=content)
    async def save_new_reply(self, comment, content, author):
        await self.add_reply(comment, content, author)


class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"].email
        self.userId = self.scope['user'].pk
        print(self.user)
        self.room_name = self.scope["url_route"]['kwargs']['news_id']
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
        news = self.room_name
        content = text_data_json["content"]
        author = self.user
        like = text_data_json["likes"]
        # selected = text_data_json["selected"]
        # count = text_data_json["count"]

        comment = text_data_json["comment"]
        if like == 'comment':
            await self.save_new_news(news,content, author)
        if like == 'post':
            await self.save_like(self.userId)
        if like == 'reply':
            await self.save_new_reply(comment, content, author)
        if like == 'liked':
            await self.discard_like(self.userId)
        # like_count = str(self.total_likes())
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "news_fields", "news": news,"author": author, "content": content, "comment": comment, "likes":like}
            # , 'selected': selected, 'count':count
        )
        # print(f'Received message from {self.channel_name}: {message}')

    # Receive message from room group
    async def news_fields(self, event):
        news = event["news"]
        like = event['likes']
        # tags = event["tags"]
        author = self.user
        content = event["content"]
        comment = event["comment"]
        # selected = await self.total_array()
        # count =  await self.total_likes()
        # print(selected, count)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"news": news, "author": author, "content": content, 'comment': comment, 'likes': like}))



    
    @database_sync_to_async
    def add_news(self, news,content, author):
        account = Account.objects.get(email=author)
        news = News.objects.get(pk=news)

        return Comment.objects.create(author=account,news=news,content=content)
        
    async def save_new_news(self, news, content, author):
        await self.add_news(news, content, author)
    

    @database_sync_to_async
    def add_like(self, usr):
        news = News.objects.get(pk=self.room_name)
        
        return news.likes.add(usr)
    async def save_like(self,usr):
        await self.add_like(usr)
    
    @database_sync_to_async
    def remove_like(self, usr):
        news = News.objects.get(pk=self.room_name)
        
        return news.likes.remove(usr)
    async def discard_like(self,usr):
        await self.remove_like(usr)

    # @database_sync_to_async
    # def get_likes(self):
    #     selected = News.objects.get(pk=self.room_name).likes.values_list('email', flat=True)
    #     selected = list(selected)
    #     count = len(selected)  
    #     return count
    # async def total_likes(self):
    #     await self.get_likes()
    
    # @database_sync_to_async
    # def get_array(self):
    #     selected = News.objects.get(pk=self.room_name).likes.values_list('email', flat=True)
    #     selected = list(selected)
    #     return selected
    
    # async def total_array(self):
    #     await self.get_array()

    @database_sync_to_async
    def add_reply(self, comment, content, author):
        account = Account.objects.get(email=author)
        comment = Comment.objects.get(pk=comment)
        return Replies.objects.create(author=account,comment=comment,content=content)
    
    async def save_new_reply(self, comment, content, author):
        await self.add_reply(comment, content, author)
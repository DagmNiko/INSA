from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/blogs/(?P<blog_id>\d+)/$", consumers.BlogConsumer.as_asgi()),
    re_path(r"ws/news/(?P<news_id>\d+)/$", consumers.NewsConsumer.as_asgi()),
]
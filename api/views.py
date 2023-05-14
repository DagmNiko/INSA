from django.shortcuts import render
from accounts.models import Account

from core.models import Blog
from .serializers import BlogSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def InsaApi(request):
    api_urls = {
        'blogs':'blogs/',
        'blog-detail':'blogs/<int:pk>/',
        'home': 'home/',
        'videos': 'videos/',
        'video-detail': 'videos/<int:pk>/',
        'news':'news/',
        'news-detail': 'news/<int:pk>/',
        'users': 'accounts/',
        'user-detail': 'accounts/<int:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogDetail(request, pk):
    blog = Blog.objects.get(pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['GET'])
def users(request):
    users = Account.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = Account.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
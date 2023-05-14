from django.urls import path
from .views import *

urlpatterns = [
    path('', InsaApi, name='api-overview'),
    path('blogs/', blogs, name='api-blogs'),
    path('blogs/<int:pk>',blogDetail, name='api-blog-detail'),
    path('accounts/', users, name='api-users'),
    path('accounts/<int:pk>',userDetail, name='api-user-detail'),
]

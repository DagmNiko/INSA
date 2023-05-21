from . import views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('blogs/', views.blogs, name='blogs'),
    path('AddBlog/', views.addBlog, name='add-blogs'),
    path('AddTOCBlogs/', views.addTOCBlogs, name='add-toc-blogs'),
    path('blogs/<int:blog_id>/', views.BlogDetail, name='blog-detail'),
    path('blogs/update/<int:pk>', views.updateBlog.as_view(), name='blog-update'),
    # path('blogs/delete/<int:pk>', views.deleteBlog.as_view(), name='blog-delete'),

    path('videos/', views.videos, name='videos'),
    path('videos/<int:pk>/', views.videoDetail, name="video-detail"), 
    path('AddVideos/', views.addVideo, name="add-videos"),

    path('news/', views.news, name="news"),
    path('news/<int:news_id>/', views.newsDetail, name="news-detail"), 
    path('AddTOCNews/', views.addTOCNews, name='add-toc-news'),
    path('AddNews/', views.addNews, name="add-news"),

    path('contactUs/', views.contacts, name='contact-us')
    # path('like/<int:pk>/', views.LikeNews, name="like_news"), 
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
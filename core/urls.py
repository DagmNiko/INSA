from . import views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('AddBlog/1/', views.addBlog, name='add-blogs'),
    path('AddBlog/2/', views.addTOC, name='add-toc'),
    path('blogs/<int:blog_id>/', views.BlogDetail, name='blog-detail'),
    path('blogs/delete/<int:pk>', views.deleteBlog.as_view(), name='blog-delete'),
    path('blogs/update/<int:pk>', views.updateBlog.as_view(), name='blog-update'),
    path('videos/', views.videos, name='videos'),
    path('videos/<int:pk>/', views.videoDetail, name="video-detail"), 
    path('AddVideos/', views.addVideo, name="add-videos")
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
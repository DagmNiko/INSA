from . import views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('AddBlog/1/', views.addBlog, name='add-blogs'),
    path('AddBlog/2/', views.addTOC, name='add-toc'),
    path('blogs/<int:blog_id>/', views.BlogDetail, name='blog-detail')
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
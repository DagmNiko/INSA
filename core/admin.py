from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')

class VideoAdimin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')

class NewsAdimin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')

class CommentAdimin(admin.ModelAdmin):
    list_display = ('author', 'date_posted')

class ReplyAdimin(admin.ModelAdmin):
    list_display = ('author', 'date_posted')

class TagAdimin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Video, VideoAdimin)
admin.site.register(News, NewsAdimin)
admin.site.register(Comment, CommentAdimin)
admin.site.register(Replies, ReplyAdimin)
admin.site.register(Tag, TagAdimin)
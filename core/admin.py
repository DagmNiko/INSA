from typing import Any
from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_posted')

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_posted')

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class TOCAdmin(admin.ModelAdmin):
    list_display = ['TOCtitle', 'placeId']

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['email', 'age', 'application_deadline', 'applied_date'] 



admin.site.register(Blog, BlogAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Replies, ReplyAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(TableOfContent,TOCAdmin)
admin.site.register(TalentApplication,ApplicationAdmin)
admin.site.register(ProofImages)
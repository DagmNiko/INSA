from django import forms
from django.forms import ModelForm

from core.models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            # 'content': forms.Textarea(attrs={'id': 'contenter'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'id': 'tags'}),
            'likes': forms.CheckboxSelectMultiple(attrs={'id': 'likes'}),
            'image': forms.FileInput(attrs={'id': 'image'}),
            'referral': forms.URLInput(attrs={'id': 'referral'}),
        }

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'tags': forms.CheckboxSelectMultiple(),
            'thumbnail': forms.FileInput(),
            'referral': forms.CheckboxSelectMultiple(),
        }
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'class': 'comment', 'placeholder': 'Write your comment here...'})
        }

class ReplyForm(ModelForm):
    class Meta:
        model = Replies
        fields = '__all__'
        widgets = {
            'content': forms.TextInput(attrs={'class': 'content', 'placeholder': 'Write your replies here...'})
        }



class TOCForm(ModelForm):
    class Meta:
        model = TableOfContent
        fields = '__all__'
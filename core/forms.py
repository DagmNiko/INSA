from django import forms
from django.forms import ModelForm

from core.models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            'content': forms.Textarea(attrs={'id': 'content'}),
            # 'tags': forms.CheckboxSelectMultiple(attrs={'id': 'tags'}),
            'image': forms.FileInput(attrs={'id': 'image'}),
            'referral': forms.URLInput(attrs={'id': 'referral'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        # widgets = {
        #     'author': forms.TextInput(attrs={'id': 'title'}),
        #     'content': forms.Textarea(attrs={'id': 'content'}),
        #     'tags': forms.CheckboxSelectMultiple(attrs={'id': 'tags'}),
        #     'image': forms.FileInput(attrs={'id': 'image'}),
        #     'referral': forms.URLInput(attrs={'id': 'referral'}),
        # }
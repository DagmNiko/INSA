from django.shortcuts import get_object_or_404, redirect, render
from core.forms import *

from core.models import *

# Create your views here.
def home(request):
    blog = Blog.objects.all().order_by('date_posted')
    video = Video.objects.all().order_by('date_posted')
    news = News.objects.all().order_by('date_posted')
    # tags = Tag.objects.all().order_by('-pk')

    context = {
        'blog': blog,
        'video': video,
        'news': news,
        # 'tags': tags,
    }
    return render(request, 'home.html', context)

def blogs(request):
    blog = Blog.objects.all().order_by('date_posted')
    context = {
        'blog': blog
    }
    return render(request, 'blogs.html', context)

def addBlog(request):
    form = BlogForm()
    # former = get_object_or_404(Blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'addBlog.html', context)

def BlogDetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('-pk')
    form = CommentForm()
    # former = get_object_or_404(Blog)
    # if request.method == 'POST':
    #     form = CommentForm(request.POST, request.FILES)
    #     if form.is_valid():
            
    #         form.save()
            
    # else:
    #     form = CommentForm()
    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
        'blog_id': blog_id
    }
    return render(request, 'blogDetail.html', context)
from django.shortcuts import get_object_or_404, redirect, render
from core.forms import *
from django.views.generic import DeleteView, UpdateView
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
    toc = TOCForm()
    # former = get_object_or_404(Blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # toc.save()
            form.save()
            return redirect('add-toc')
            
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'addBlog.html', context)

def addTOC(request):
    form = TOCForm()
    # former = get_object_or_404(Blog)
    if request.method == 'POST':
        form = TOCForm(request.POST)
        title = None
        placeId = None
        if form.is_valid():
            print(request.POST)
            for req in request.POST:
                if 'TOCtitle' in req:
                   title = request.POST[req]
                   if req[8:]:
                       placeId = request.POST[f'placeId{req[8:]}']
                   else:
                       placeId = request.POST['placeId']
                   TableOfContent.objects.create(blog=Blog.objects.get(pk=request.POST['blog']), TOCtitle=title, placeId=placeId)  
                    
            return redirect('blogs')
            
    else:
        form = TOCForm()
    context = {
        'toc': form,
    }
    return render(request, 'addTOC.html', context)

def BlogDetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('-pk')
    replies = Replies.objects.all().order_by('-pk')
    form = CommentForm()
    toc = TableOfContent.objects.filter(blog=blog)
    replyForm = ReplyForm()
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
        'blog_id': blog_id,
        'replyForm': replyForm,
        'replies': replies,
        'toc': toc,
    }
    return render(request, 'blogDetail.html', context)

class updateBlog(UpdateView):
    model = Blog
    template_name = 'updateBlog.html'
    fields = ['image', 'title', 'content', 'referral','tags']




class deleteBlog(DeleteView):
    model = Blog
    template_name = "deleteBlog.html"


def videos(request):
    video = Video.objects.all().order_by('date_posted')
    context = {
        'video': video
    }
    return render(request, 'videos.html', context)

def videoDetail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {
        'video': video
    }
    return render(request, 'videoDetail.html', context)


def addVideo(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos')
            
    else:
        form = VideoForm()
    context = {
        'form': form
    }
    return render(request, 'addVideo.html', context)
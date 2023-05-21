from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from core.forms import *
from django.views.generic import DeleteView, UpdateView
from core.models import *
from django.core.mail import send_mail
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
            # toc.save()
            form.save()
            return redirect('add-toc-blogs')
            
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'addBlog.html', context)

def addTOCBlogs(request):
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
                if 'placeId' in req:
                    if req[8:]:
                        placeId = request.POST[f'placeId{req[7:]}']
                    else:
                        placeId = request.POST['placeId']
                    TableOfContent.objects.create(blog=Blog.objects.get(pk=request.POST['blog']), TOCtitle=title, placeId=placeId)  
                    
            return redirect('blogs')
            
    else:
        form = TOCForm()
    context = {
        'toc': form,
    }
    return render(request, 'addTOCBlogs.html', context)


def addTOCNews(request):
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
                if 'placeId' in req:
                    if req[8:]:
                        placeId = request.POST[f'placeId{req[7:]}']
                    else:
                        placeId = request.POST['placeId']
                    TableOfContent.objects.create(news=News.objects.get(pk=request.POST['news']), TOCtitle=title, placeId=placeId)  
                    
            return redirect('news')
            
    else:
        form = TOCForm()
    context = {
        'toc': form,
    }
    return render(request, 'addTOCNews.html', context)


def BlogDetail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('-pk')
    replies = Replies.objects.all().order_by('-pk')
    form = CommentForm()
    toc = TableOfContent.objects.filter(blog=blog)
    replyForm = ReplyForm()
    likes = Blog.objects.get(pk=blog_id)
    likes = likes.total_likes()
    selected = list(Blog.objects.get(pk=blog_id).likes.values_list('email', flat=True))
    accountSelected = str(request.user.email) in selected

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
        'blog_id': blog_id,
        'replyForm': replyForm,
        'replies': replies,
        'toc': toc,
        'likes': likes,
        'selected':accountSelected
    }
    return render(request, 'blogDetail.html', context)

class updateBlog(UpdateView):
    model = Blog
    template_name = 'updateBlog.html'
    fields = ['image', 'title', 'content', 'referral','tags']


def videos(request):
    video = Video.objects.all().order_by('date_posted')
    context = {
        'video': video
    }
    return render(request, 'videos.html', context)

def videoDetail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    recommended = []
    for vid in Video.objects.all():
        splitted = vid.title.split(" ")
        for i in splitted:
            if vid.pk != pk:
                if i.lower() in video.title.lower().split(" "):
                    recommended.append(vid.title)
                    
    print(recommended)
    context = {
        'video': video,
        'recommended': recommended
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

def news(request):
    news = News.objects.all().order_by('date_posted')
    context = {
        'news': news
    }
    return render(request, 'news.html', context)

def newsDetail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    comments = Comment.objects.filter(news=news).order_by('-pk')
    replies = Replies.objects.all().order_by('-pk')
    form = CommentForm()
    likes = get_object_or_404(News, pk=news_id)
    likes = likes.total_likes()
    selected = list(News.objects.get(pk=news_id).likes.values_list('email', flat=True))
    accountSelected = str(request.user.email) in selected
    try:
        toc = TableOfContent.objects.filter(news=news)
    except:
        toc = ''
    replyForm = ReplyForm()

    context = {
        'news': news,
        'comments': comments,
        'form': form,
        'news_id': news_id,
        'replyForm': replyForm,
        'replies': replies,
        'toc': toc,
        'likes': likes,
        'selected':accountSelected
    }
    return render(request, 'newsDetai.html', context)



def addNews(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add-toc-news')
            
    else:
        form = NewsForm()
    context = {
        'form': form
    }
    return render(request, 'addNews.html', context)


def contacts(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            send_mail(
                f'Feedback from user{request.user.email}(request.user.username): {request.POST["subject"]}',
                request.POST['body'],
                request.user.email,
                ["dagmniko79@gmail.com"]

            )
            form.save()
            
            return redirect('home')
            
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contacts.html', context)

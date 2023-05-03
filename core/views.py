from django.shortcuts import get_object_or_404, render

from core.models import Blog, News, Tag, Video

# Create your views here.
def home(request):
    blog = Blog.objects.all().order_by('date_posted')
    video = Video.objects.all().order_by('date_posted')
    news = News.objects.all().order_by('date_posted')
    tags = Tag.objects.all().order_by('-pk')

    context = {
        'blog': blog,
        'video': video,
        'news': news,
        'tags': tags,
    }
    return render(request, 'home.html', context)
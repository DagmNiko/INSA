from django.db import models
from django.forms import ValidationError
from accounts.models import Account

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to="BlogImages", blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    referral = models.URLField()
    tags = models.ManyToManyField('Tag', blank=True)
    #like
    #share
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('blog-detail', args=[str(self.id)])

class Video(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='userVideos')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    referral = models.URLField()
    tags = models.ManyToManyField('Tag', blank=True)
    #like
    #share

    def __str__(self):
        return self.title
    
class News(models.Model):
    image = models.ImageField(upload_to="NewsImages", blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    referral = models.URLField()
    tags = models.ManyToManyField('Tag', blank=True)
    #like
    #share

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    image = models.ImageField(upload_to="TagImages", blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name






class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if (self.blog and self.video and self.news) or (self.blog and self.video and not self.news) or (not self.blog and self.news and self.video) or (self.blog and self.news and not self.video):
            raise ValidationError("You can enter only one of the three fields(blog, video or news)")
        
    def __str__(self):
        return self.content
    

class Replies(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #like

    def __str__(self):
        return self.content
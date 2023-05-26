from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from accounts.models import Account




# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='BlogImages/main/', blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    referral = models.ManyToManyField('Referral', related_name='blog_referrals', blank=True) 
    tags = models.ManyToManyField('Tag', blank=True)
    likes = models.ManyToManyField(Account, related_name='blog_likes', blank=True)
    #share
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class TableOfContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey('News', on_delete=models.CASCADE, blank=True, null=True)
    TOCtitle = models.CharField(max_length=550)
    placeId = models.CharField(max_length=150) #more like an id for its section like #home
    def clean(self):
        if (self.blog and self.news) or (not self.blog and not self.news):
            raise ValidationError("You can enter only one of the two fields(blog or news)")
        

class Video(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    content = models.FileField(upload_to='userVideos')
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    referral = models.ManyToManyField('Referral', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    is_redirect = models.BooleanField(default=False)
    redirect_url = models.URLField(
        blank=True,
        null=True,
        help_text="Enter your youtube or other page's url."
    )
    likes = models.ManyToManyField(Account, related_name='video_likes', blank=True)
    #share
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
class Referral(models.Model):
    blogObj = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs')
    videoObj = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True, related_name='videos')
    newsObj = models.ForeignKey('News', on_delete=models.CASCADE, blank=True, null=True, related_name='news')
    link = models.TextField()
    alt = models.CharField(max_length=25, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if (self.blog and self.video and self.news) or (self.blog and self.video and not self.news) or (not self.blog and self.news and self.video) or (self.blog and self.news and not self.video):
            raise ValidationError("You can enter only one of the three fields(blog, video or news)")
        
    def __str__(self):
        return self.alt or self.link
    
class News(models.Model):
    image = models.ImageField(upload_to="NewsImages", blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    referral = models.ManyToManyField('Referral', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    likes = models.ManyToManyField(Account, related_name='news_likes', blank=True)
    #share
    def total_likes(self):
        return self.likes.count()
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
    
class Contact(models.Model):
    subject = models.CharField(max_length=225)
    body = models.TextField()

    def __str__(self):
        return self.subject

class ProofImages(models.Model):
    image = models.ImageField(upload_to="ApplicantsProof", blank=True, null=True)
    to = models.ForeignKey('TalentApplication', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

class TalentApplication(models.Model):
    email = models.ForeignKey(Account, on_delete=models.CASCADE)
    talent = models.CharField(max_length=225)
    age = models.IntegerField()
    # proof_images = models.ForeignKey(ProofImages, on_delete=models.CASCADE)
    define_yourself = models.TextField(max_length=300)
    application_deadline = models.DateField()
    applied_date = models.DateField(auto_now=True)
    def save_model(self, request, obj, form, change):
        if self.email.applied == True:
            raise ValidationError("You have already applied")
        else:
            self.email.applied = True
            return super().save()
    def __str__(self):
        return self.application_deadline
    

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    referral = models.URLField()
    tags = models.ManyToManyField('Tag')
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
    author = models.CharField(max_length=100)
    referral = models.URLField()
    tags = models.ManyToManyField('Tag')
    #like
    #share

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    referral = models.URLField()
    tags = models.ManyToManyField('Tag')
    #like
    #share

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name






class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == "draft" and self.pub_date is not None:
            raise ValidationErro("Draft entries may not have a publication date.")
    def __str__(self):
        return self.content
    
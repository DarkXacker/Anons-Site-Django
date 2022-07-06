from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Anon(models.Model):
    name = models.CharField(max_length=300)
    body = RichTextField()
    image = models.ImageField(upload_to='anons/images/')
    video = models.FileField(upload_to='anons/videos/', blank=True)
    telegram = models.CharField(max_length=90, blank=True)
    instagram = models.CharField(max_length=90, blank=True)
    youtube = models.CharField(max_length=120, blank=True)
    likes = models.ManyToManyField(get_user_model(), related_name='blog_posts', blank=True)

    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return self.name + ": " + str(self.videofile)

    def total_views(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('anons_detail', args=[str(self.id)])

class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(
        Anon, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.blogpost_connected} - {self.author}"

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .utils import get_slug


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    like_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_votes")
    unlike_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="unlike_votes")

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_date']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:news-details', kwargs={'slug': self.slug})

    def get_like_url(self):
        return reverse('news:like-news', kwargs={'slug': self.slug})

    def get_unlike_url(self):
        return reverse('news:unlike-news', kwargs={'slug': self.slug})

    def get_comment_url(self):
        return reverse('news:leave-comment-news', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content}"

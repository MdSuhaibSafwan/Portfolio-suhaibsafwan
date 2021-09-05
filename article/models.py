from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from random import choice
from string import ascii_letters


def get_random_letters():
    return "".join(choice(ascii_letters) for i in range(10))


def slugify_title(title):
    return slugify(title) + get_random_letters()


class ArticleBar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = self.slug
        if slug is None:
            self.slug = slugify_title(self.title)

        return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article_bar = models.ForeignKey(ArticleBar, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=150)
    body = models.TextField()
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = self.slug
        if slug is None:
            self.slug = slugify_title(self.title)

        return super().save(*args, **kwargs)


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=150)
    body = models.TextField()
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return self.title

    def save(self, *args, **kwargs):
        slug = self.slug
        if slug is None:
            self.slug = slugify_title(self.title)

        return super().save(*args, **kwargs)

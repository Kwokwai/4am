#-*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Topic(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=256, blank=True)
    author = models.CharField(max_length=100)
    author_img = models.CharField(max_length=100, default=None)
    content = models.TextField(default=None)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey('Category')
    views = models.IntegerField(default=0)
    # responce_count =models.IntegerField(default=0)
    # last_response = models.ForeignKey()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic:detail', kwargs={'topic_id': self.id})


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name
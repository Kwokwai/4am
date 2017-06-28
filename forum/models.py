#-*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from user.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib import admin
from django import forms


class Topic(models.Model):
    title = models.CharField(max_length=36)
    abstract = models.CharField(max_length=256, blank=True)
    author = models.ForeignKey(UserProfile)
    content = RichTextUploadingField(verbose_name='正文')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey('Category', null=True)
    views = models.IntegerField(default=0)
    # responce_count =models.IntegerField(default=0)
    # last_response = models.ForeignKey()

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'topic_id': self.id})


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name






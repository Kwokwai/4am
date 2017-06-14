#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from forum.models import Topic, Tag, Category
from django.http import HttpResponse


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        topic_list = Topic.objects.all()
        return topic_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        return super(IndexView, self).get_context_data(**kwargs)


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'detail.html'
    context_object_name = "topic"
    pk_url_kwarg = 'topic_id'

    def get_object(self, *args, **kwargs):
        obj = super(TopicDetailView, self).get_object()
        return obj

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        kwargs['tag_list'] = Tag.objects.all().order_by('tag_name')
        return super(TopicDetailView, self).get_context_data(**kwargs)


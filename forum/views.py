#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django.views.generic import DetailView
from forum.models import Topic, Category
from forum.forms import TopicCreateForm
from user.models import UserProfile
from comments.forms import CommentForm


class IndexView(ListView):
    model = Topic
    template_name = 'index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        topic_list = Topic.objects.all()
        return topic_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('category_name')
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'detail.html'
    context_object_name = "topic"
    pk_url_kwarg = 'topic_id'

    def get(self, request, *args, **kwargs):
        response = super(TopicDetailView, self).get(self, request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list,
        })
        return context


class TopicCreateView(FormView):
    model = Topic
    template_name = 'create.html'
    form_class = TopicCreateForm

    success_url = '/'

    def form_valid(self, form):
        user = UserProfile.objects.get(user=self.request.user)
        form.save(user)
        return super(TopicCreateView, self).form_valid(form)


class CategoryView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        topic_list = Topic.objects.filter(categories=self.kwargs['categories_id'])
        return topic_list

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_list = Category.objects.all().order_by('category_name')
        context.update({
            'category_list': category_list,
        })
        return context


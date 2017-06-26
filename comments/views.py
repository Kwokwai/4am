#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from forum.models import Topic
from .forms import CommentForm
from user.models import UserProfile
from django.views.generic import DetailView


def post_comment(request, topic_id):
    post = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = user
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'detail.html', context=context)
    return redirect(post)



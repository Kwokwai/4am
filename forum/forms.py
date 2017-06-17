#-*-coding:utf-8 -*-
from django import forms
from forum.models import Topic
from django.contrib.auth.models import User


class TopicCreateForm(forms.Form):

    class Meta:
        model = Topic
        fields = ['title', 'author', 'content']

    title = forms.CharField(
        label=u'文章标题',
        max_length=50,
        error_messages={'required': u'标题不能为空'},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'文章标题', 'title': u'必填'}),
    )

    content = forms.CharField(
        label=u'内容',
        min_length=10,
        widget=forms.Textarea(),
    )

    def save(self, username):
        tittle = self.cleaned_data['title']
        content = self.cleaned_data['content']
        topic = Topic(
            author=username,
            title=tittle,
            content=content
        )

        topic.save()
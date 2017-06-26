#-*-coding:utf-8 -*-
from django import forms
from ckeditor.fields import RichTextField, RichTextFormField
from forum.models import Topic, Category


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
        widget=forms.Textarea(attrs={
                              'style': 'height: 400px;width:810px'})
    )

    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label=u'板块',
        error_messages={'required': u'文章分类不能为空'},
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def save(self, user):
        tittle = self.cleaned_data['title']
        content = self.cleaned_data['content']
        categories = self.cleaned_data['categories']
        topic = Topic(
            author=user,
            title=tittle,
            categories=categories,
            content=content
        )

        topic.save()



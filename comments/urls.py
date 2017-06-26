from django.conf.urls import url
from django.contrib import admin
from comments import views


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<topic_id>[0-9]+)/$', views.post_comment, name='post_comment'),
]
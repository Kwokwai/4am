from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.TopicDetailView.as_view(), name='detail'),
    url(r'^topic_create/$', views.TopicCreateView.as_view(), name='create'),

]

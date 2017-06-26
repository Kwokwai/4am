from django.conf.urls import url
from forum import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.TopicDetailView.as_view(), name='detail'),
    url(r'^category/(?P<categories_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^topic_create/$', views.TopicCreateView.as_view(), name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

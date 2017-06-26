from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^user_info/(?P<user_id>\d+)/$', views.UserInfoView.as_view(), name='info'),
    url(r'^updateinfo', views.updateInfo, name='updateinfo'),
    url(r'^create', views.signaturechange, name='create'),
]


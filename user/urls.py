from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]


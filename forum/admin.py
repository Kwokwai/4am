from django.contrib import admin
from forum.models import Tag, Topic, Category


admin.site.register(Topic)
admin.site.register(Tag)
admin.site.register(Category)


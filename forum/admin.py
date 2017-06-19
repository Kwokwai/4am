from django.contrib import admin
from forum.models import Tag, Topic, Category
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

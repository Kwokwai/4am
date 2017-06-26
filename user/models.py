#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from fouram import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(max_length=128, blank=True, default="这人很帅,什么都没说")
    avatar = models.ImageField(upload_to="user/img", blank=True, default="user/default.jpg")

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'UserProfile'

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = UserProfile.objects.get(user=self.user)
                self.pk = p.pk
            except UserProfile.DoesNotExist:
                pass
        super(UserProfile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:info', kwargs={'user_id': self.id})


def creaet_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(creaet_user_profile, sender=User)



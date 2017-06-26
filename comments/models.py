from django.db import models
from user.models import UserProfile
from django.core.urlresolvers import reverse


class Comment(models.Model):
    name = models.ForeignKey(UserProfile)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('forum.Topic')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('comments:post_comment', kwargs={'topic_id': self.id})
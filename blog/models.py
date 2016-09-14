from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField()
    link = models.TextField(default="")
    link.blank = True
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def __unicode__(self):
    def __str__(self):
        return self.title.encode('utf8')


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    html = models.TextField(default="")
    html.blank = True
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text.encode('utf8')

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)



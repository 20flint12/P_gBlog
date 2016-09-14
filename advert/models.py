from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Advert(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50, default='Title')
    text = models.TextField()
    html = models.TextField(default="")
    html.blank = True

    # created_date = models.DateTimeField(default=timezone.now)
    # approved_ad = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def approve(self):
        self.approved_ad = True
        self.save()

    def __str__(self):
        return self.text.encode('utf8')

    # def approved_ads(self):
    #     return self.comments.filter(approved_ads=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

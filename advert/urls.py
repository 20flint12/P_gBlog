#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^adverts/$', views.advert_list, name='advert_list'),
    url(r'^advert/(?P<pk>[0-9]+)/$', views.advert_detail, name='advert_detail'),
    url(r'^advert/new/$', views.advert_new, name='advert_new'),
    url(r'^advert/(?P<pk>[0-9]+)/edit/$', views.advert_edit, name='advert_edit'),
    url(r'^advert/drafts/$', views.advert_draft_list, name='advert_draft_list'),
    url(r'^advert/(?P<pk>\d+)/publish/$', views.advert_publish, name='advert_publish'),
    url(r'^advert/(?P<pk>\d+)/remove/$', views.advert_remove, name='advert_remove'),

]

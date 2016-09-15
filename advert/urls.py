#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^adverts/$', views.advert_list, name='advert_list'),
    url(r'^advert/(?P<pk>[0-9]+)/$', views.advert_detail, name='advert_detail'),

]

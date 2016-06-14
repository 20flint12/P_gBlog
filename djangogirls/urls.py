# from django.conf.urls import include, url
# from django.contrib import admin
# from django.views.generic.base import RedirectView
#
#
# urlpatterns = [
#     # Redirect old links:
#     url(r'^pages/in-your-city/$', RedirectView.as_view(url='/organize/', permanent=True)),
#     url(r'^admin$', RedirectView.as_view(url='/admin/', permanent=True)),
#
#     # Admin link for password reset
#     # See: https://github.com/darklow/django-suit/blob/92a745d72935622220eca80edfce779419c30094/suit/templates/admin/login.html#L61
#     url(r'^admin/password_reset/$',
#         RedirectView.as_view(url='/account/password_reset', permanent=True),
#         name='admin_password_reset'),
#
#     # Regular links:
#     url(r'^community/', include('jobs.urls', namespace='jobs')),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^pages/', include('django.contrib.flatpages.urls')),
#     url(r'^account/', include('django.contrib.auth.urls')),
#     url(r'', include('applications.urls', namespace='applications')),
#     url(r'', include('core.urls', namespace='core')),
# ]


# *****************************************************************************
# *****************************************************************************
# *****************************************************************************

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^accounts/login/$', views.login, name='login'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # url(r'^accounts/logout/$', views.logout, name='logout', {'next_page': '/'}),

    url(r'', include('blog.urls')),

]

# import settings
# import os
# if settings.DEBUG404:
#     urlpatterns += [
#     url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
#     # {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
#     ]


# http://stackoverflow.com/questions/1296629/django-template-tag-how-to-send-next-page-in-url-auth-logout


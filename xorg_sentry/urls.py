from django.conf.urls.defaults import patterns, url, include
from sentry.conf.urls import handler404, handler500
from sentry.conf.urls import urlpatterns as sentry_urlpatterns


urlpatterns = patterns('',
    url(r'^xorgauth/', include('django_authgroupex.urls', namespace='authgroupex')),
    url(r'^login/', 'xorg_sentry.views.login', name='xlogin'),
) + sentry_urlpatterns

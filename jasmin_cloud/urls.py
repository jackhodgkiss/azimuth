"""
URL definitions for the ``jasmin_cloud`` Django app.
"""

from django.conf.urls import url, include

from . import views


UUID_REGEX = r'[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}'

app_name = 'jasmin_cloud'
urlpatterns = [
    url(r'^authenticate/$', views.authenticate, name = 'authenticate'),
    url(r'^session/$', views.session, name = 'session'),
    url(r'^tenancies/$', views.tenancies, name = 'tenancies'),
    url(r'^tenancies/(?P<tenant>'+ UUID_REGEX + r')/', include([
        url(r'^quotas/$', views.quotas, name = 'quotas'),
        url(r'^images/$', views.images, name = 'images'),
        url(r'^images/(?P<image>' + UUID_REGEX + r')/$',
            views.image_details,
            name = 'image_details'),
        url(r'^sizes/$', views.sizes, name = 'sizes'),
        url(r'^sizes/(?P<size>[a-z0-9-]+)/$',
            views.size_details,
            name = 'size_details'),
        url(r'^external_ips/$', views.external_ips, name = 'external_ips'),
        url(r'^external_ips/(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/$',
            views.external_ip_details,
            name = 'external_ip_details'),
        url(r'^volumes/$', views.volumes, name = 'volumes'),
        url(r'^volumes/(?P<volume>' + UUID_REGEX + r')/$',
            views.volume_details,
            name = 'volume_details'),
        url(r'^machines/$', views.machines, name = 'machines'),
        url(r'^machines/(?P<machine>' + UUID_REGEX + r')/', include([
            url(r'^$', views.machine_details, name = 'machine_details'),
            url(r'^start/$', views.machine_start, name = 'machine_start'),
            url(r'^stop/$', views.machine_stop, name = 'machine_stop'),
            url(r'^restart/$', views.machine_restart, name = 'machine_restart'),
        ])),
    ])),
]

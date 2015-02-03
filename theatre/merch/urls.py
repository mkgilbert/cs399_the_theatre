from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'merch.views.index', name='merch'),
                       url(r'^/(?P<inventory_id>\d+)', 'merch.views.detail',
                           name='merch_detail'),
)
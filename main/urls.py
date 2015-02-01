from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# main access point to site
	url(r'^$', 'main.views.index', name='index'),
    # all performances
    url(r'^performance$', 'main.views.performance.all', name='performance'),
    # performance detail: performance/1234
    url(r'^performance/(?P<id>\d+)', 'main.views.performance.detail', name='performance.id'),
    # performance detail: performance/1234/some_descriptive_text_for_useability_that_doesnt matter
    url(r'^performance/(?P<id>\d+)/(?P<slug>.+)', 'main.views.performance.detail',
        name='performance.id.slug'),
	url(r'^location$', 'main.views.location', name='location'),
	# merch
	url(r'^merch$', 'merch.views.index', name='merch'),
	url(r'^merch/(?P<inventory_id>\d+)/$', 'merch.views.detail', name='merch_detail'),
    # admin
    url(r'^admin/', include(admin.site.urls)),
)

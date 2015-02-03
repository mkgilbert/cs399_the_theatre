from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'main.views.index', name='index'),
	url(r'^location$', 'main.views.location', name='location'),

)

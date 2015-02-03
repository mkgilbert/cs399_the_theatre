from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'shows.views.all', name='all'),
                       # show detail: show/1234
                       url(r'^/(?P<id>\d+)', 'shows.views.detail',
                           name='id'),
                       # show detail: show/1234/some_descriptive_text_for_useability_that_doesnt matter
                       url(r'^/(?P<id>\d+)/(?P<slug>.+)',
                           'shows.views.detail',
                           name='id.slug')
)

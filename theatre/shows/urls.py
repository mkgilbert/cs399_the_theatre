from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'shows.views.all', name='all'),
                       # show detail: show/1234
                       url(r'^/(?P<show_id>\d+)/ticket/(?P<ticket_id>\d+)',
                           'shows.views.ticket',
                           name='ticket'),
                       url(r'^/(?P<id>\d+)', 'shows.views.detail',
                           name='id'),

)

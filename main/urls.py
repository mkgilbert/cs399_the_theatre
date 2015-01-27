from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	# main access point to site
	# Don't know if index is a good name or not...
	url(r'^$', 'main.views.index.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

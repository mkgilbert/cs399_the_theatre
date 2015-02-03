from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',  # main access point to site
                       (r'^', include('main.urls', namespace='main',
                                       app_name='main')),
                       (r'^shows', include('shows.urls', namespace='shows',
                                           app_name='shows')),
                       (r'^merch', include('merch.urls', namespace='merch',
                                           app_name='merch')),
                       (r'^menu', include('menu.urls', namespace='menu',
                                           app_name='menu')),
                       # admin
                       url(r'^admin/', include(admin.site.urls)),
)

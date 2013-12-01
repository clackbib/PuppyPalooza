from django.conf.urls import patterns, include, url
from home.feeds import LatestPuppyFeed
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin


urlpatterns = patterns('sourcecode.views',

    url(r'^$', 'sourcecode'),
)

from django.conf.urls import patterns, include, url
from home.feeds import LatestPuppyFeed

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #HOME URL
    url(r'^$', 'home.views.home_page'),
    url(r'^home/', include('home.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'member/', include('login.urls')),
    url(r'^feeds/puppies/$', LatestPuppyFeed(), name='feed_puppies'),
    (r'^accounts/', include('allauth.urls')),
    #url(r'^youtube/', include('django_youtube.urls')),
    # Examples:
    # url(r'^$', 'PuppyPalooza.views.home', name='home'),
    # url(r'^PuppyPalooza/', include('PuppyPalooza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include("admin.site.urls")),
)

from shop.models import Puppy
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse


class LatestPuppyFeed(Feed):
    title = "Latest Puppies !"
    link='' # URI of site
    description='Latest Puppy Entries'

    def items(self):
        return Puppy.objects.all()[:5]

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('home.views.home_page')




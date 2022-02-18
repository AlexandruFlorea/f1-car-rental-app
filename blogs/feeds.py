from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blogs.models import Post


class LatestPostsFeed(Feed):
    """
    The title, link, and description correspond to the standard RSS <title>, <link> and <description> elements.
    """
    title = 'My blog'
    link = ''
    description = 'New posts from my blog'

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

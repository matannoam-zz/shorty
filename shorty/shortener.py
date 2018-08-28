from string import letters, digits
from random import choice


class Shortener(object):

    def __init__(self):
        self.short_urls = {}

    def shorten(self, original_url):
        for short_url, long_url in self.short_urls.iteritems():
            if long_url == original_url:
                return short_url

        short_url = choice(letters + digits)
        while short_url in self.short_urls:
            short_url = choice(letters + digits)
        self.short_urls[short_url] = original_url
        return short_url

from string import letters, digits
from random import choice


class Shortener(object):

    def __init__(self):
        self.shortened_urls = {}

    def shorten(self, original_url):
        for short_url, long_url in self.shortened_urls.iteritems():
            if long_url == original_url:
                return short_url

        short_url = choice(letters + digits)
        while short_url in self.shortened_urls:
            short_url = choice(letters + digits)
        self.shortened_urls[short_url] = original_url
        return short_url

    def lengthen(self, short_url):
        return self.shortened_urls[short_url]

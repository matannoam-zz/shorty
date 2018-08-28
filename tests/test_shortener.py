from unittest import TestCase

from shorty.shortener import Shortener


class ShortenerTests(TestCase):

    def setUp(self):
        self.shortener = Shortener()

    def test_shorten_returns_a_short_url(self):
        original_url = 'http://www.google.com'

        short_url = self.shortener.shorten(original_url)

        self.assertIsNotNone(short_url)

    def test_shorten_a_different_url_returns_a_different_short_url(self):
        first_original_url = 'http://www.google.com'
        second_original_url = 'http://www.github.com'

        first_short_url = self.shortener.shorten(first_original_url)
        second_short_url = self.shortener.shorten(second_original_url)

        self.assertNotEqual(first_short_url, second_short_url)

    def test_shorten_same_url_returns_same_short_url(self):
        original_url = 'http://www.google.com'

        first_short_url = self.shortener.shorten(original_url)
        second_short_url = self.shortener.shorten(original_url)

        self.assertEqual(first_short_url, second_short_url)

from django.test import TestCase
from .models import ShortenedURL


class ShortenedURLTestCase(TestCase):
    def test_url_creation(self):
        url = ShortenedURL.objects.create(
            original_url="http://example.com", short_code="abc123"
        )
        self.assertEqual(url.short_code, "abc123")

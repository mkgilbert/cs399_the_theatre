from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from main.urls import urlpatterns
from bs4 import BeautifulSoup
import requests


class TestLinks(TestCase):
    """
    Use the test client to get all of the views and test that the correct template was used.
    """

    def test_broken_links(self):
        def check_link(href):
            if "//" in href:
                self.assertEqual(requests.get(href).status_code, 200)
            elif '/static/' in href:
                # remove static for django
                static = href.replace('/static/', '')
                self.assertIsNotNone(finders.find(static))
            else:
                self.assertEqual(self.client.get(href).status_code, 200)

        for pattern in urlpatterns:
            if not hasattr(pattern, 'name'):
                continue

            url = reverse(pattern.name)
            response = self.client.get(url)
            soup = BeautifulSoup(str(response))
            a = soup.find_all('a')
            for link in a:
                # get link address
                href = link.get('href')

                if href is None or len(href) == 0 or href[0] == '#':
                    continue

                check_link(href)

            img = soup.find_all('img')
            for link in img:
                href = link.get('src')
                if href is None or len(href) == 0 or href[0] == '#':
                    continue

                check_link(href)




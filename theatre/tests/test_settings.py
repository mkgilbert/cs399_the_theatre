from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from theatre.settings import STATICFILES_DIRS, BASE_DIR


class TestSettings(TestCase):
    def test_static_config(self):
        """
        Tests the static file configuration to make sure
        that the app looks in the static folder paths.
        """
        result = finders.find('dummy_filename')
        searched_locations = finders.searched_locations
        for d in STATICFILES_DIRS:
            self.assertIn(d, searched_locations)

from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from urls import urlpatterns
from views import all, detail


class TestViews(TestCase):
    """
    Use the test client to get all of the views and test that the correct template was used.
    """

    def setUp(self):
        self.factory = RequestFactory()

    def test_show_url(self):
        url = reverse('shows:all')
        self.assertEqual(url, '/shows')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shows/all.html')

    def test_show_view(self):
        # Create an instance of a GET request.
        request = self.factory.get('/shows')
        response = all(request)
        self.assertEqual(response.status_code, 200)

    def test_show_detail_url(self):
        url = reverse('shows:id', kwargs={'id': 1})
        self.assertEqual(url, '/shows/1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shows/detail.html')

    def test_show_detail_view(self):
        # Create an instance of a GET request.
        request = self.factory.get('/shows/1/test')
        response = detail(request, id=1, slug='test')
        self.assertEqual(response.status_code, 200)
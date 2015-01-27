from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from main.views import index, performance
from main.urls import urlpatterns



class TestViews(TestCase):
    """
    Use the test client to get all of the views and test that the correct template was used.
    """

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(url, '/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        
    def test_performance_url(self):
        url = reverse('performance')
        self.assertEqual(url, '/performance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'performance/all.html')

    def test_performance_view(self):
        # Create an instance of a GET request.
        request = self.factory.get('/performance')
        response = performance.all(request)
        self.assertEqual(response.status_code, 200)

    def test_performance_detail_url(self):
        url = reverse('performance.id', kwargs={'id': 1})
        self.assertEqual(url, '/performance/1')
        url = reverse('performance.id.slug', kwargs={'id': 1, 'slug': 'test'})
        self.assertEqual(url, '/performance/1/test')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'performance/detail.html')

    def test_performance_detail_view(self):
        # Create an instance of a GET request.
        request = self.factory.get('/performance/1/test')
        response = performance.detail(request, id=1, slug='test')
        self.assertEqual(response.status_code, 200)
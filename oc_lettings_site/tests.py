def test_dummy():
    assert 1

from django.test import TestCase
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_custom_404_view(self):
        response = self.client.get('/url-inexistante/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


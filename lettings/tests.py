from django.test import TestCase
from django.urls import reverse
from .models import Letting, Address


class LettingViewTests(TestCase):

    def setUp(self):

        self.test_address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TC'
        )

    def test_lettings_index_view(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings_index.html')

    def test_letting_view(self):
        letting = Letting.objects.create(title='Test Letting', address=self.test_address)
        response = self.client.get(reverse('letting', args=(letting.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'letting.html')
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, self.test_address)

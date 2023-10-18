from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Profile, User
from .views import profiles_index, profile


class ProfileViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_profile = Profile.objects.create(user=self.test_user, favorite_city='Test City')

    def test_profiles_index_view(self):
        request = self.factory.get(reverse('profiles_index'))
        response = profiles_index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles_index.html')

    def test_profile_view(self):
        request = self.factory.get(reverse('profile', args=('testuser',)))
        response = profile(request, username='testuser')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, 'Test City')

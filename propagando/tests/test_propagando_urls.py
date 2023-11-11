from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class PropagandoURLTest(TestCase):
    def test_if_url_propagando_home_is_correct(self):
        propagando_home = reverse('propagando:home')
        self.assertEqual(propagando_home, '/')

from django.test import TestCase
from django.urls import reverse, resolve
from propagando import views

# Create your tests here.


class PropagandoViewTest(TestCase):
    def test_propagando_view_home_is_correct(self):
        view = resolve(reverse('propagando:home'))
        self.assertIs(view.func, views.home)

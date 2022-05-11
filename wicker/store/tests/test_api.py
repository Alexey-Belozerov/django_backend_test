from django.urls import reverse
from rest_framework.test import APITestCase


class WickerApiTestCase(APITestCase):

    def test_get(self):
        url = reverse('wicker-list')

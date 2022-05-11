from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerApiTestCase(APITestCase):

    def test_get(self):
        wicker_1 = Wicker.objects.create(name='Test wicker 1', price=1500)
        wicker_2 = Wicker.objects.create(name='Test wicker 2', price=2815)
        url = reverse('wicker-list')
        response = self.client.get(url)
        serializer_data = WickerSerializer([wicker_1, wicker_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

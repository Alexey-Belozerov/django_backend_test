from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerApiTestCase(APITestCase):
    def SetUp(self):
        self.wicker_1 = Wicker.objects.create(name='Test wicker 1', price=1500, author_name='Author 1')
        self.wicker_2 = Wicker.objects.create(name='Test wicker 2', price=2815, author_name='Author 2')
        self.wicker_3 = Wicker.objects.create(name='Test wicker 3', price=2815, author_name='Author 3')

    def test_get(self):
        url = reverse('wicker-list')
        response = self.client.get(url)
        serializer_data = WickerSerializer([self.wicker_1, self.wicker_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

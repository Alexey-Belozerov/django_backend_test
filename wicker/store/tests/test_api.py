import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.wicker_1 = Wicker.objects.create(name='Test wicker 1', price=1500,
                                              author_name='Author 1')
        self.wicker_2 = Wicker.objects.create(name='Test wicker 2', price=2815,
                                              author_name='Author 1')
        self.wicker_3 = Wicker.objects.create(name='Test wicker 3 Author 1',
                                              price=2815, author_name='Author 2')

    def test_get(self):
        url = reverse('wicker-list')
        response = self.client.get(url)
        serializer_data = WickerSerializer([self.wicker_1, self.wicker_2, self.wicker_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('wicker-list')
        response = self.client.get(url, data={'price': 2815})
        serializer_data = WickerSerializer([self.wicker_2, self.wicker_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('wicker-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = WickerSerializer([self.wicker_1, self.wicker_2,
                                            self.wicker_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('wicker-list')
        response = self.client.get(url, data={'price': 2815})
        serializer_data = WickerSerializer([self.wicker_2,
                                            self.wicker_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Wicker.objects.all().count())
        url = reverse('wicker-list')
        data = {
            'name': 'Корзина Победа',
            'price': '3700.00',
            'author_name': 'Красная Виктория'
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Wicker.objects.all().count())

    def test_update(self):
        url = reverse('wicker-list')
        data = {
            'name': self.wicker_1.name,
            'price': 4200,
            'author_name': self.wicker_1.author_name
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

from django.test import TestCase

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerSerializerTestCase(TestCase):

    def test_ok(self):
        wicker_1 = Wicker.objects.create(name='Test wicker 1', price=1500)
        wicker_2 = Wicker.objects.create(name='Test wicker 2', price=2815)
        data = WickerSerializer([wicker_1, wicker_2], many=True).data
        expected_data = [
            {
                'id': wicker_1.id,
                'name': 'Test wicker 1',
                'price': '1500.00'
            },
            {
                'id': wicker_2.id,
                'name': 'Test wicker 2',
                'price': '2815.00'
            },
        ]
        self.assertEqual(expected_data, data)
from django.test import TestCase

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerSerializerTestCase(TestCase):

    def test_ok(self):
        wicker_1 = Wicker.objects.create(name='Test wicker 1', price=1500)
        wicker_2 = Wicker.objects.create(name='Test wicker 2', price=2815)
        data = WickerSerializer([wicker_1, wicker_2], many=True).data


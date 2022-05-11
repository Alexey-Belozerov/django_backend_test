from rest_framework.serializers import ModelSerializer

from store.models import Wicker


class WickerSerializer(ModelSerializer):
    class Meta:
        model = Wicker
        fields = '__all__'
        # fields = ['id', 'name', 'price']

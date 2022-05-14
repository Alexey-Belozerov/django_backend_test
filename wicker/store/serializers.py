from rest_framework.serializers import ModelSerializer

from store.models import Wicker, UserWickerRelation


class WickerSerializer(ModelSerializer):
    class Meta:
        model = Wicker
        fields = '__all__'
        # fields = ['id', 'name', 'price', 'author_name', 'owner']


class UserWickerRelationSerializer(ModelSerializer):
    class Meta:
        model = UserWickerRelation
        fields = '__all__'
        fields = ['wicker', 'like', 'in_bookmarks', 'rate']

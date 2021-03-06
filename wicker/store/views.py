from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from store.models import Wicker, UserWickerRelation
from store.permissions import IsOwnerOrStaffOrReadOnly
from store.serializers import WickerSerializer, UserWickerRelationSerializer


class WickerViewSet(ModelViewSet):
    queryset = Wicker.objects.all()
    serializer_class = WickerSerializer
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserWickerRelationViewSet(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserWickerRelation.objects.all()
    serializer_class = UserWickerRelationSerializer
    lookup_field = 'wicker'

    def get_object(self):
        obj, _ = UserWickerRelation.objects.get_or_create(user=self.request.user,
                                                          wicker_id=self.kwargs['wicker'])
        return obj


def auth(request):
    return render(request, 'oauth.html')

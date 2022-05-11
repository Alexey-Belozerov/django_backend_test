from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerViewSet(ModelViewSet):
    queryset = Wicker.objects.all()
    serializer_class = WickerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['price']


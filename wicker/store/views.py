from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from store.models import Wicker
from store.serializers import WickerSerializer


class WickerViewSet(ModelViewSet):
    queryset = Wicker.objects.all()
    serializer_class = WickerSerializer


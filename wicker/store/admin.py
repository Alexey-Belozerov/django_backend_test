from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Wicker


@admin.register(Wicker)
class WickerAdmin(ModelAdmin):
    list_display = ['name', 'price']

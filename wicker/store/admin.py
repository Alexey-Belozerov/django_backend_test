from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Wicker, UserWickerRelation


@admin.register(Wicker)
class WickerAdmin(ModelAdmin):
    list_display = ['name', 'price', 'author_name']


@admin.register(UserWickerRelation)
class UserWickerRelationAdmin(ModelAdmin):
    pass

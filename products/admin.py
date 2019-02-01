from django.contrib import admin

from .models import Tag, Item


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

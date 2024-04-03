from django.contrib import admin
from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id', 'title', 'description', 'image')
    search_fields = ('title', 'id')
    list_editable = ("title", 'description', 'image')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id', "title", 'description', 'amount', 'price', 'image', 'active', 'shop', 'category')
    search_fields = ('title', 'id')
    list_filter = ('amount', 'price',)
    list_editable = ("title", 'description', 'amount', 'price', 'image', 'active', 'shop', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ("id", 'title', 'description')
    search_fields = ('title', 'id')
    list_editable = ("title", 'description')
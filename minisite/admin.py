from django.contrib import admin
from minisite.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_created', 'date_updated')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'price', 'stock', 'date_created', 'date_updated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
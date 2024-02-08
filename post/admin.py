from django.contrib import admin

from post.models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id']
    list_editable = ['price']

    fields = ['id', 'name', 'photo', 'price']
    readonly_fields = ['id']


# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)

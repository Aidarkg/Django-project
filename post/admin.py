from django.contrib import admin

from post.models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id']
    list_editable = ['price']

    fields = ['id', 'user', 'name', 'photo', 'price', 'categories', 'description']
    readonly_fields = ['id']



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'created_at']
    list_display_links = ['id', 'text', 'user']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Review)

from django.contrib import admin

from post.models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id']
    list_editable = ['price']

    fields = ['id', 'name', 'photo', 'price', 'description']
    readonly_fields = ['id']



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','text', 'created_at']
    list_display_links = ['id', 'text']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Review)

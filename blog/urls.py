from django.contrib import admin
from django.urls import path
from post.views import hello_view, data_view, goodbye_view, products_view, main_view, category_view, product_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_view),
    path('current_data/', data_view),
    path('goodby/', goodbye_view),
    path('', main_view),
    path('products/', products_view),
    path('categories/', category_view),
    path('product/<int:product_id>/', product_detail_view),
]

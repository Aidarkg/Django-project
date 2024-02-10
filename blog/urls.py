from django.contrib import admin
from django.urls import path
from post.views import hello_view, data_view, goodbye_view, products_view, \
    main_view, category_view, product_detail_view, product_create_view, category_create_view, \
    review_create_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_view),
    path('current_data/', data_view),
    path('goodby/', goodbye_view),
    path('', main_view),
    path('products/', products_view, name='products_list'),
    path('categories/', category_view),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products/create/', product_create_view),
    path('category/create/', category_create_view),
    path('product/<int:product_id>/review/', review_create_view, name='review_create')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from post.views import hello_view, get_current_time, goodbye_view, main_view, review_create_view, \
    HelloView, ProductView, CategoryView, ProductDeatilView, ProductCreateView, CategoryCreateView,\
    ProductUpdateView



urlpatterns = [
    path('hello/', hello_view),
    path('hello2/', HelloView.as_view()),
    path('current_time/', get_current_time, name='get_current_time'),
    path('goodby/', goodbye_view),
    path('', main_view),
    path('products/', ProductView.as_view(), name='products_list'),
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('products/<int:product_id>/', ProductDeatilView.as_view(), name='product_detail'),
    path('products/<int:product_id>/edit_product/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/create/', ProductCreateView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('products/<int:product_id>/review/', review_create_view, name='review_create'),
]
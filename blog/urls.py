from django.contrib import admin
from django.urls import path
from post.views import hello_view, data_view, goodbye_view, products_view, \
    main_view, category_view, product_detail_view, product_create_view, category_create_view, \
    review_create_view
from django.conf import settings
from django.conf.urls.static import static
from user import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_view),
    path('current_data/', data_view),
    path('goodby/', goodbye_view),
    path('', main_view),
    path('products/', products_view, name='products_list'),
    path('categories/', category_view, name='categories_list'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('products/create/', product_create_view),
    path('category/create/', category_create_view),
    path('product/<int:product_id>/review/', review_create_view, name='review_create'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/', views.verify_view, name='verify'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

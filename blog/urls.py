from django.contrib import admin
from django.urls import path
from post.views import hello_view, data_view, goodbye_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello_view),
    path('current_data/', data_view),
    path('goodby/', goodbye_view)
]

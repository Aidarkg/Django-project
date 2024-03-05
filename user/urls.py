from django.urls import path
from user import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('verify/', views.verify_view, name='verify'),
    path('profile_update/', views.profile_update_view),
]
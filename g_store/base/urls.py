from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('show_product/', include('inventory.urls')),
]
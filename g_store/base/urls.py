from . import views
from django.urls import path, include



urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('show_product/', include('inventory.urls')),
    path('update-profile/', views.update_profile, name='update'),
]
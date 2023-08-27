from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk>/', views.show_product, name='show_product'),
    
]
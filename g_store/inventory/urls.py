from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk>/', views.show_product, name='show_product'),
    path('<str:pk>/purchase', views.buy_product, name='buy_product'),
    path('billing/<int:purchase_id>/', views.billing, name='billing'),
    path('', views.search, name='search'),
]
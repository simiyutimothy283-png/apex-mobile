from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail_view, name='cart_detail'),
    path('login/', views.login_view, name='login'),
    path('choice-picks/', views.choice_picks, name='choice_picks'),
]
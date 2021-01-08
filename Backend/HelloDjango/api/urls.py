from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainDataView.as_view()),  # Основная информация для сайта
    path('home/', views.HomePageDataView.as_view()),  # Главная страница
    path('home/<slug:slug>', views.HomePageDataView.as_view()),  # Главная страница
    path('shop/future_products/<slug:slug>', views.FutureProductsView.as_view()),  # Избранные товары (хиты продаж)
    # Товары для главной по категориям
    path('shop/home_products_by_category/<city>/<category>', views.HomeProductsByCategoryView.as_view()),
    # Товары со скидкой для главной страницы
    path('shop/home_sale_products/<slug:slug>', views.HomeSaleProductsView.as_view()),
    path('product/<slug:slug>', views.ProductDetailView.as_view()),
    path('additional_products/<city>/<int:category_id>', views.AdditionalProductsView.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePageDataView.as_view()),  # Главная страница
    path('home/<slug:slug>/', views.HomePageDataView.as_view()),  # Главная страница
    path('shop/future_products/<slug:slug>/', views.FutureProductsView.as_view()),  # Избранные товары (хиты продаж)
    # Товары для главной по категориям
    path('shop/home_products_by_category/<city>/<category>/', views.HomeProductsByCategoryView.as_view()),
    # Товары со скидкой для главной страницы
    path('shop/home_sale_products/<slug:slug>/', views.HomeSaleProductsView.as_view()),
    path('product/<slug:slug>/', views.ProductDetailView.as_view()),
    path('additional_products/<int:city>/<int:pk>/', views.AdditionalProductsView.as_view()),
    path('reason_detail/<slug:slug>/<int:city_id>/', views.ReasonDetailView.as_view()),
    path('category_detail/<slug:slug>/<int:city_id>', views.CategoryDetailView.as_view()),
    path('sort_detail/<slug:slug>/<int:city_id>/', views.SortDetailView.as_view()),
    path('testimonials/', views.TestimonialsView.as_view()),
    path('policy/', views.PrivacyPolicyView.as_view()),
    path('offer/', views.PublicOfferView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contacts/', views.ContactsView.as_view()),

    path('', views.MainDataView.as_view()),  # Основная информация для сайта
]

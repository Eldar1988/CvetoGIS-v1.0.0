from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainDataView.as_view()),     # Основная информация для сайта
    path('home/', views.HomePageDataView.as_view()),    # Главная страница
    path('home/<slug:slug>', views.HomePageDataView.as_view()),    # Главная страница
]
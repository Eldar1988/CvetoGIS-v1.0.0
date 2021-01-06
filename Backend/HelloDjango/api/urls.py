from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainDataView.as_view()),     # Основная информация для сайта
]
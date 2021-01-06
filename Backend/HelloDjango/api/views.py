from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Course, City, DeliveryBranch, Category, Reason, Sort, HomePageInfo, Product
from shop.serializers import CategoryListSerializer, CitySerializer, CourseSerializer, ReasonsListSerializer, \
    SortListSerializer, HomeInfoSerializer, ProductListSerializer

from cvetogis.models import Slider
from cvetogis.serializers import SliderSerializer


class MainDataView(APIView):
    """Основная информация"""

    def get(self, request):
        response_data = {}

        cities = City.objects.all()
        cities_serializer = CitySerializer(cities, many=True)
        response_data['cities'] = cities_serializer.data

        courses = Course.objects.all()
        courses_serializer = CourseSerializer(courses, many=True)
        response_data['courses'] = courses_serializer.data

        categories = Category.objects.filter(public=True)
        categories_serializer = CategoryListSerializer(categories, many=True)
        response_data['categories'] = categories_serializer.data

        reasons = Reason.objects.filter(public=True)
        reasons_serializer = ReasonsListSerializer(reasons, many=True)
        response_data['reasons'] = reasons_serializer.data

        sorts = Sort.objects.filter(public=True)
        sorts_serializer = SortListSerializer(sorts, many=True)
        response_data['sorts'] = sorts_serializer.data

        return Response(response_data)


class HomePageDataView(APIView):
    """Главная страница"""
    def get(self, request, slug='karaganda'):
        response_data = {}

        info = HomePageInfo.objects.get(city__slug=slug)
        info_serializer = HomeInfoSerializer(info, many=False)
        response_data['homePageInfo'] = info_serializer.data

        slides = Slider.objects.all()
        slides_serializer = SliderSerializer(slides, many=True)
        response_data['slides'] = slides_serializer.data

        categories = Category.objects.filter(show_on_home_page=True, public=True, cities__slug=slug)
        categories_serializer = CategoryListSerializer(categories, many=True)
        response_data['categories'] = categories_serializer.data

        # Товары со скидкой - 2 index
        products = Product.objects.filter(show_on_home_page=True, old_price__gt=1, cities__slug=slug, public=True)
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        return Response(response_data)


class FutureProductsView(APIView):
    """Хиты продаж"""

    def get(self, request, slug):
        products = Product.objects.filter(future=True, show_on_home_page=True, cities__slug=slug, public=True)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class HomeSaleProductsView(APIView):
    """Товары со скдикой для главной"""

    def get(self, request, slug):
        products = Product.objects.filter(show_on_home_page=True, cities__slug=slug, old_price__gt=1, public=True)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class HomeProductsByCategoryView(APIView):
    """Товары по категориям для главной"""

    def get(self, request, city, category):
        products = Product.objects.filter(future=True, show_on_home_page=True, cities__slug=city,
                                          category__slug=category, public=True)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Course, City, DeliveryBranch, Category, Reason, Sort, HomePageInfo
from shop.serializers import CategoryListSerializer, CitySerializer, CourseSerializer, ReasonsListSerializer, \
    SortListSerializer, HomeInfoSerializer

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

        return Response(response_data)

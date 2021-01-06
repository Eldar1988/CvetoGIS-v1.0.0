from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Course, City, DeliveryBranch, Category, Reason, Sort
from shop.serializers import CategoryListSerializer, CitySerializer, CourseSerializer, ReasonsListSerializer, \
    SortListSerializer


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

        reasons = Reason.objects.all()
        reasons_serializer = ReasonsListSerializer(reasons, many=True)
        response_data['reasons'] = reasons_serializer.data

        sorts = Sort.objects.all()
        sorts_serializer = SortListSerializer(sorts, many=True)
        response_data['sorts'] = sorts_serializer.data

        return Response(response_data)

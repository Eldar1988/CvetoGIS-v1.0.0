from rest_framework import serializers

from .models import City, Course, HomePageInfo, Reason, Category, Sort, Product, DeliveryBranch


class HomeInfoSerializer(serializers.ModelSerializer):
    """Информация для главных страниц"""

    class Meta:
        model = HomePageInfo
        fields = '__all__'


class DeliveryBranchSerializer(serializers.ModelSerializer):
    """Районы доставки"""

    class Meta:
        model = DeliveryBranch
        exclude = ('order',)


class CitySerializer(serializers.ModelSerializer):
    """Города"""
    deliveries = DeliveryBranchSerializer(many=True)

    class Meta:
        model = City
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Валюты"""

    class Meta:
        model = Course
        fields = ('id', 'title', 'value', 'icon')


class ReasonsListSerializer(serializers.ModelSerializer):
    """Поводы список"""

    class Meta:
        model = Reason
        exclude = ('description', 'order')


class CategoryListSerializer(serializers.ModelSerializer):
    """Категории список"""

    class Meta:
        model = Category
        exclude = ('image', 'description', 'order', 'cities', 'show_on_home_page')


class SortListSerializer(serializers.ModelSerializer):
    """Сорта список"""

    class Meta:
        model = Sort
        exclude = ('description', 'image', 'order')


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    sort = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    reasons = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    cities = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Product
        exclude = ('images', 'short_description', 'description', 'future', 'visible_on_home_page', 'order',
                   'seller', 'public', 'views', 'pub_date', 'update')

from rest_framework import serializers

from .models import City, Course, HomePageInfo, Reason, Category, Sort, Product, DeliveryBranch, Size, Image, Seller


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
    miniature = serializers.SerializerMethodField('get_miniature_url')

    def get_miniature_url(self, obj):
        return obj.miniature.url

    class Meta:
        model = Category
        exclude = ('image', 'description', 'order', 'cities', 'show_on_home_page')


class SortListSerializer(serializers.ModelSerializer):
    """Сорта список"""
    miniature = serializers.SerializerMethodField('get_miniature_url')

    def get_miniature_url(self, obj):
        return obj.miniature.url

    class Meta:
        model = Sort
        exclude = ('description', 'image', 'order')


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    sort = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    reasons = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    cities = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Product
        exclude = ('short_description', 'description', 'future', 'show_on_home_page', 'order',
                   'seller', 'public', 'views', 'pub_date', 'update')


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Категория детали"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True)

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Category
        exclude = ('miniature', 'order', 'cities', 'show_on_home_page')


class SortDetailSerializer(serializers.ModelSerializer):
    """Сорт детали"""
    image = serializers.SerializerMethodField('get_image_url')
    products = ProductListSerializer(many=True)

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Sort
        exclude = ('description', 'miniature', 'order')


class ReasonsDetailSerializer(serializers.ModelSerializer):
    """Повод детали"""
    products = ProductListSerializer(many=True)

    class Meta:
        model = Reason
        exclude = ('order',)


class SizeSerializer(serializers.ModelSerializer):
    """Список размеров товара"""

    class Meta:
        model = Size
        fields = '__all__'


class ProductImagesSerializer(serializers.ModelSerializer):
    """Дополнительные изображения товара"""

    class Meta:
        model = Image
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    """Продавец"""

    class Meta:
        model = Seller
        fields = ('id', 'title', 'address', 'slug')


class ProductDetailSerializer(serializers.ModelSerializer):
    """Детали товара"""
    sort = SortListSerializer(many=True, read_only=True)
    category = CategoryListSerializer(many=False, read_only=True)
    reasons = ReasonsListSerializer(many=False, read_only=True)
    sizes = SizeSerializer(many=True, read_only=True)
    images = ProductImagesSerializer(many=True, read_only=True)
    seller = SellerSerializer(many=False)

    class Meta:
        model = Product
        exclude = ('pub_date', 'update', 'views', 'public', 'order', 'suggest', 'show_on_home_page', 'future')

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Course, City, DeliveryBranch, Category, Reason, Sort, HomePageInfo, Product
from shop.serializers import CategoryListSerializer, CitySerializer, CourseSerializer, ReasonsListSerializer, \
    SortListSerializer, HomeInfoSerializer, ProductListSerializer, ProductDetailSerializer, ReasonsDetailSerializer, \
    CategoryDetailSerializer, SortDetailSerializer

from cvetogis.models import Slider, Testimonial, Benefit, AboutInfo, SocialNetwork, PrivacyPolicy, PublicOffer, Contact
from cvetogis.serializers import SliderSerializer, TestimonialsSerializer, BenefitsSerializer, ShortAboutInfoSerializer, \
    SocialNetworksSerializer, PrivacyPolicySerializer, PublicOfferSerializer, FullAboutInfoSerializer, ContactsSerializer


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

        benefits = Benefit.objects.all()
        benefits_serializer = BenefitsSerializer(benefits, many=True)
        response_data['benefits'] = benefits_serializer.data

        about = AboutInfo.objects.last()
        about_serializer = ShortAboutInfoSerializer(about, many=False)
        response_data['about'] = about_serializer.data

        socials = SocialNetwork.objects.all()
        socials_serializer = SocialNetworksSerializer(socials, many=True)
        response_data['socials'] = socials_serializer.data

        contacts = Contact.objects.last()
        contacts_serializer = ContactsSerializer(contacts, many=False)
        response_data['contacts'] = contacts_serializer.data

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

        products = Product.objects.filter(show_on_home_page=True, old_price__gt=1, cities__slug=slug, public=True)
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        testimonials = Testimonial.objects.filter(public=True, show_on_home_page=True)[:10]
        testimonials_serializer = TestimonialsSerializer(testimonials, many=True)
        response_data['testimonials'] = testimonials_serializer.data

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


class ProductDetailView(APIView):
    """Детали товара"""

    def get(self, request, slug):
        response_data = {}
        product = Product.objects.get(slug=slug)
        product_serializer = ProductDetailSerializer(product, many=False)
        response_data['product'] = product_serializer.data
        product.views += 1
        product.save()

        return Response(response_data)


class AdditionalProductsView(APIView):
    """Дополнительные товары"""

    def get(self, request, city, category_id):
        city = city.split(',')
        response_data = {}
        toys = Product.objects.filter(suggest=True, public=True, cities__title__in=city).distinct()
        toys_serializer = ProductListSerializer(toys, many=True)
        response_data['toys'] = toys_serializer.data

        products = Product.objects.filter(category_id=category_id, public=True, cities__title__in=city).distinct()[:12]
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        return Response(response_data)


class ReasonDetailView(APIView):
    """Повод детали"""

    def get(self, request, slug, city_id):
        response_data = {}
        reason = Reason.objects.get(slug=slug)
        reason_serializer = ReasonsDetailSerializer(reason, many=False)
        response_data['reason'] = reason_serializer.data

        products = Product.objects.filter(reasons__id=reason.id, cities__id=city_id, public=True)
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        return Response(response_data)


class CategoryDetailView(APIView):
    """Категория детали"""

    def get(self, request, slug, city_id):
        response_data = {}
        category = Category.objects.get(slug=slug)
        category_serializer = CategoryDetailSerializer(category, many=False)
        response_data['category'] = category_serializer.data

        products = Product.objects.filter(category_id=category.id, cities__id=city_id, public=True)
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        return Response(response_data)


class SortDetailView(APIView):
    """Сорт детали"""

    def get(self, request, slug, city_id):
        response_data = {}
        sort = Sort.objects.get(slug=slug)
        sort_serializer = SortDetailSerializer(sort, many=False)
        response_data['sort'] = sort_serializer.data

        products = Product.objects.filter(sort__id=sort.id, cities__id=city_id, public=True)
        products_serializer = ProductListSerializer(products, many=True)
        response_data['products'] = products_serializer.data

        return Response(response_data)


class TestimonialsView(APIView):
    """Отзывы"""

    def get(self, request):
        testimonials = Testimonial.objects.filter(public=True)
        serializer = TestimonialsSerializer(testimonials, many=True)
        return Response(serializer.data)

    def post(self, request):
        testimonial = TestimonialsSerializer(data=request.data)
        if testimonial.is_valid():
            testimonial.save()

            return Response(status=201)


class PrivacyPolicyView(APIView):
    """Политика конфиденциальности"""
    def get(self, request):
        policy = PrivacyPolicy.objects.last()
        serializer = PrivacyPolicySerializer(policy, many=False)
        return Response(serializer.data)


class PublicOfferView(APIView):
    """Публичная оферта"""
    def get(self, request):
        offer = PublicOffer.objects.last()
        serializer = PublicOfferSerializer(offer, many=False)
        return Response(serializer.data)


class AboutView(APIView):
    """Информация о компании"""
    def get(self, request):
        info = AboutInfo.objects.last()
        serializer = FullAboutInfoSerializer(info, many=False)
        return Response(serializer.data)


class ContactsView(APIView):
    """Контакты"""
    def get(self, request):
        contacts = Contact.objects.last()
        serializer = ContactsSerializer(contacts, many=False)
        return Response(serializer.data)

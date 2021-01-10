from rest_framework import serializers

from .models import Slider, AboutInfo, Testimonial, Benefit, SocialNetwork, PrivacyPolicy, PublicOffer, Contact


class SliderSerializer(serializers.ModelSerializer):
    """Слайды"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Slider
        fields = '__all__'


class ShortAboutInfoSerializer(serializers.ModelSerializer):
    """Краткая информация о компании"""

    class Meta:
        model = AboutInfo
        exclude = ('info', 'requisite')


class FullAboutInfoSerializer(serializers.ModelSerializer):
    """Краткая информация о компании"""
    logo = serializers.SerializerMethodField('get_logo_url')

    def get_logo_url(self, obj):
        return obj.logo.url

    class Meta:
        model = AboutInfo
        fields = '__all__'


class BenefitsSerializer(serializers.ModelSerializer):
    """"Преимущества"""

    class Meta:
        model = Benefit
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    """"Отзывы"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url

    class Meta:
        model = Testimonial
        exclude = ('public',)


class SocialNetworksSerializer(serializers.ModelSerializer):
    """Социальные сети"""

    class Meta:
        model = SocialNetwork
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    """Политика конфиденциальности"""

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class PublicOfferSerializer(serializers.ModelSerializer):
    """Публичная оферта"""

    class Meta:
        model = PublicOffer
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    """Контакты"""

    class Meta:
        model = Contact
        fields = '__all__'

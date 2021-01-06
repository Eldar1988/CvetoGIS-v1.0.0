from rest_framework import serializers

from .models import Slider


class SliderSerializer(serializers.ModelSerializer):
    """Слайды"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = Slider
        fields = '__all__'

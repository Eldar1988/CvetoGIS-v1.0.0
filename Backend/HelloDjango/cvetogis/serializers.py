from rest_framework import serializers

from .models import Slider


class SliderSerializer(serializers.ModelSerializer):
    """Слайды"""

    class Meta:
        model = Slider
        fields = '__all__'

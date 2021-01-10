from rest_framework import serializers

from .models import CallBack, PaymentMethod, Order


class CallBackSerializer(serializers.ModelSerializer):
    """Заявки на обратный звонок"""

    class Meta:
        model = CallBack
        exclude = ('notice', 'date', 'update', 'complete')


class PaymentMethodsSerializer(serializers.ModelSerializer):
    """Способы оплаты"""
    image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = PaymentMethod
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Заказ"""

    class Meta:
        model = Order
        exclude = ('info', 'date', 'update', 'complete')

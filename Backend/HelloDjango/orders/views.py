from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CallBack, Order, PaymentMethod
from .serializers import CallBackSerializer, PaymentMethodsSerializer, OrderSerializer


class CallBackView(APIView):
    """Заявки на обратный звонок"""
    def post(self, request):
        serializer = CallBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        return Response(status=400)


class PaymentMethodsView(APIView):
    """Способы оплаты"""
    def get(self, request):
        payments = PaymentMethod.objects.all()
        serializer = PaymentMethodsSerializer(payments, many=True)
        return Response(serializer.data)


class NewOrder(APIView):
    """Новый заказ"""
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        print(serializer.errors)

        return Response(status=400)


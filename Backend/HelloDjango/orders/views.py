from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CallBack
from .serializers import CallBackSerializer


class CallBackView(APIView):
    """Заявки на обратный звонок"""
    def post(self, request):
        serializer = CallBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        return Response(status=400)

from django.urls import path
from . import views


urlpatterns = [
    path('call_back/', views.CallBackView.as_view())
]
from django.urls import path
from . import views


urlpatterns = [
    path('call_back/', views.CallBackView.as_view()),
    path('payments/', views.PaymentMethodsView.as_view()),
    path('new_order/', views.NewOrder.as_view()),
]

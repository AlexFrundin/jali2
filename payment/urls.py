from django.urls import path
from . import views


urlpatterns = [
    path('process/', views.PaymentProcess, name='process'),
    path('done/', views.PaymentDone, name='done'),
    path('canceled/', views.PaymentCanceled, name='canceled')
]

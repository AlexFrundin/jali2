from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.mainpage, name='index'),
    path('news/<int:id>', views.snews, name='snews'),
    path('news', views.news, name='news'),
    path('service/<int:id>', views.usluga, name='usluga'),
    path('p/<str:link>', views.page, name='page'),
    path('contact', views.contact, name='contact')
]

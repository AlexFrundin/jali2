from django.urls import path
from mainapp import views

urlpatterns = [

    path('', views.mainpage, name='index'),
    path('pay', views.addconsultation, name='addconsultation'),
    path('news/<int:id>', views.snews, name='snews'),
    path('news', views.news, name='news'),
    path('service/<int:id>', views.usluga, name='usluga'),
    path('p/<str:link>', views.page, name='page'),
    #url(r'list', views.list, name='list'),
    #url(r'copy', views.copy, name='copy'),
]

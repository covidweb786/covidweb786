from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('prediction', views.prediction, name='prediction'),
    path('about', views.about, name='about')

]

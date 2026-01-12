from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_color,name='home'),
    path('favorite-color',views.get_color,name='favorite_color'),
    path('result',views.result,name='result')
]
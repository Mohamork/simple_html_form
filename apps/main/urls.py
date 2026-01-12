from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_color,name='get the color'),
    path('result',views.result,name='result')
]
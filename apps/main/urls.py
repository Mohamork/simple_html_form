from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_color,name='your-favorite-color')
]
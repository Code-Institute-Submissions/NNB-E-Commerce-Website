from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_products, name='display_products')
]
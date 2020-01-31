from django.urls import path

from .views import price_list, price_list_by_category

urlpatterns = [
    path('', price_list, name='price-list'),
    path('prices-by-category', price_list_by_category, name='price-list-category'),

]

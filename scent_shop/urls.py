from django.urls import path

import scent_shop.views
from scent_shop.views import ProductListView,  ProductDetailView, CategoryProductListView, BrandProductListView, Search

urlpatterns = [
    path('', ProductListView.as_view(), name="shop-home"),
    path("search/", Search.as_view(), name="search"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="shop-detail"),
    path("brand/<int:pk>/", BrandProductListView.as_view(), name="shop-brand"),
    path("category/<int:pk>/", CategoryProductListView.as_view(), name="shop-category"),
    path("basket/", scent_shop.views.basket, name="basket")
]

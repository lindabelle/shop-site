from django.urls import path
from scent_shop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("", views.home, name="scent_shop-home"),
    path("brand/", views.brand, name="scent_shop-brand"),
    path("gourmet/", views.gourmet, name="scent_shop-gourmet"),
    path("floral/", views.floral, name="scent_shop-floral"),
    path("woody/", views.woody, name="scent_shop-woody"),
    path("oriental/", views.oriental, name="scent_shop-oriental"),
    path("base/", views.base, name="scent_shop-base"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

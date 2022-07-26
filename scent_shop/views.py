from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand, Basket, User
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect


class ProductListView(ListView):
    model = Product
    template_name = 'scent_shop/home.html'
    context_object_name = 'products'
    paginate_by = 6


class ProductDetailView(DetailView):
    model = Product


class CategoryProductListView(ListView):
    model = Product
    template_name = 'scent_shop/category.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs.get("pk"))
        return Product.objects.filter(category=category)


class BrandProductListView(ListView):
    model = Product
    template_name = 'scent_shop/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        brand = get_object_or_404(Brand, pk=self.kwargs.get("pk"))
        return Product.objects.filter(brand=brand)


class Search(ListView):
    template_name = "scent_shop/base.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


def basket(request):
    content = {}
    return render(request, 'scent_shop/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(product=product).first()
    user = self.request.user
    if not basket:
        basket = Basket(product=product)
    basket.item_total += 1
    basket.save()
    return HttpResponseRedirect(reverse('scent_shop:basket'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'scent_shop/basket.html', content)


def base(request):
    return render(request, "scent_shop/base.html")





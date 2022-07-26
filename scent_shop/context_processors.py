from .models import Category, Brand


def get_category_name(request):
    categories = Category.objects.all()
    return {'category': categories}


def get_brand_name(request):
    brands = Brand.objects.all()
    return {'brand': brands}

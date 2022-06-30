from django.http import HttpResponse
from django.shortcuts import render
from .models import Pics


descriptions = [
            {
                'name': 'Fat Electrician',
                'brand': 'ELDO',
                'description': 'White vetiver splattered on the asphalt of Time Square”, the fragrance juxtaposes the dry, earthy transparency of vetiver with the sweeter, balsamic smokiness of opoponax and myrrh.',
                'price': 140,
                'year': 2009
                },
                {
                'name': 'Like This',
                'brand': 'ELDO',
                'description': 'A radical fragrance that soothes the fire under the milky skin. A warm perfume, cooled by ginger. If this perfume was a light, it would be an orange glow.',
                'price': 140,
                'year': 2010

            },
]



def home(request):
    images = Pics.objects
    return render(request, "scent_shop/home.html", {'images': images})


def brand(request):
    return render(request, "scent_shop/brand.html")


def gourmet(request):
    return render(request, "scent_shop/gourmet.html")


def floral(request):
    return render(request, "scent_shop/floral.html")


def woody(request):
    return render(request, "scent_shop/woody.html")


def oriental(request):
    return render(request, "scent_shop/oriental.html")

def base(request):
    return render(request, "scent_shop/base.html")





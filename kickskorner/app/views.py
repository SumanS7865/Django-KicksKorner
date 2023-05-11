from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,

    }

    return render(request, 'store/store.html', context)

def category_page(request, category_slug=None):
    categories = None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products': products,
    }

    return render(request, 'store/category.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }

    return render(request, 'store/product-detail.html',context)

def contact(request):
    return render (request, 'contact.html')

def about(request):
    return render (request, 'about.html')

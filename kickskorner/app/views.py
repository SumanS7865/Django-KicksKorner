from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.
def store(request):
    products        = Product.objects.all().filter(is_available=True).order_by('id')
    paginator       = Paginator(products, 8)
    page            = request.GET.get('page')
    paged_products  = paginator.get_page(page)

    context = {
        'products': paged_products,

    }

    return render(request, 'store/store.html', context)

def category_page(request, category_slug=None):
    categories = None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_available=True).order_by('id')
        paginator       = Paginator(products, 6)
        page            = request.GET.get('page')
        paged_products  = paginator.get_page(page)
    else:
        products        = Product.objects.all().filter(is_available=True).order_by('id')
        paginator       = Paginator(products, 6)
        page            = request.GET.get('page')
        paged_products  = paginator.get_page(page)

    context = {
        'products': paged_products,

    }
    return render(request, 'store/category.html', context)




def product_detail(request, category_slug, product_slug):
    try:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator       = Paginator(products, 8)
        page            = request.GET.get('page')
        paged_products  = paginator.get_page(page)
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
    except Exception as e:
        raise e

    context = {
        'products': paged_products,
        'single_product': single_product,
        'in_cart': in_cart,
    }

    return render(request, 'store/product-detail.html',context)

def contact(request):
    return render (request, 'contact.html')

def about(request):
    return render (request, 'about.html')

def error(request):
    return render(request, 'store/404.html')


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))

    context = {
        'products' : products,
    }

    return render(request, 'store/search.html', context)
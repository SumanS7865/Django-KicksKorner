from django.shortcuts import render, HttpResponse, redirect
from app.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator       = Paginator(products, 8)
    page            = request.GET.get('page')
    paged_products  = paginator.get_page(page)

    context = {
        'products': paged_products,
    }

    return render (request, 'index.html', context)

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product, Slider, Staff
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import ReviewRating
from .forms import ReviewForm


# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True).order_by("id")
    paginator = Paginator(products, 8)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)
    sliders = Slider.objects.all()
    context = {
        "products": paged_products,
        "sliders": sliders,
    }

    return render(request, "store/store.html", context)


def category_page(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True
        ).order_by("id")
        paginator = Paginator(products, 6)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 6)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)

    context = {
        "products": paged_products,
    }
    return render(request, "store/category.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 8)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
        )
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=single_product
        ).exists()
    except Exception as e:
        raise e

    context = {
        "products": paged_products,
        "single_product": single_product,
        "in_cart": in_cart,
    }

    return render(request, "store/product-detail.html", context)


def contact(request):
    name = request.POST.get("name")
    message = request.POST.get("message")
    sender = request.POST.get("email")
    subject = f"New message from {name}."

    if subject and message and sender:
        email_message = f"{message}\n\n\nSender Email: {sender}"
        send_mail(
            subject,
            email_message,
            sender,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        success_message = "Message sent successfully!"
        messages.success(request, success_message)
    return render(request, "contact.html")


def about(request):
    staffs = Staff.objects.all()
    context = {
        "staffs": staffs,
    }
    return render(request, "about.html", context)


def error(request):
    return render(request, "store/404.html")


def search(request):
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            products = Product.objects.order_by("-created_date").filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )

    context = {
        "products": products,
    }

    return render(request, "store/search.html", context)


def submit_review(request, product_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        try:
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id
            )
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, "Thank you! your review has been updtated")
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data["subject"]
                data.rating = form.cleaned_data["rating"]
                data.review = form.cleaned_data["review"]
                data.ip = request.META.get("REMOTE_ADDR")
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
            messages.success(request, "Thank you! your review has been Submitted.")
            return redirect(url)

from django.shortcuts import render ,redirect, HttpResponse
from app.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    # get the product
    product = Product.objects.get(id=product_id)
    try:
        #  get the cart using the cart_id
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  #cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,

        )
        cart_item.save()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += int(cart_item.product.selling_price) * int(cart_item.quantity)
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        pass  #just ignore
    templates_name = ['store/cart.html', 'index.html']


    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
    }
    return render (request, templates_name, context)


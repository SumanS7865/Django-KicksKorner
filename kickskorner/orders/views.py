from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from carts.models import *
from .forms import OrderForm
from .models import *
import datetime
import json
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(
        user=request.user, is_ordered=False, order_number=body["orderID"]
    )

    # store transaction details inside Payment model
    payment = Payment(
        user=request.user,
        payment_id=body["transID"],
        payment_method=body["payment_method"],
        amount_paid=order.order_total,
        status=body["status"],
    )
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    # move the cart items to Order Product table
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.selling_price
        orderproduct.ordered = True
        orderproduct.save()

        cart_item = CartItem.objects.get(id=item.id)
        product_variation = cart_item.variations.all()
        orderproduct = OrderProduct.objects.get(id=orderproduct.id)
        orderproduct.variations.set(product_variation)
        orderproduct.save()

    # reduce the quantity of the sold products
    product = Product.objects.get(id=item.product_id)
    product.stock -= item.quantity
    product.save()

    # clear cart
    CartItem.objects.filter(user=request.user).delete()

    # send order received email to customer
    mail_subject = "Thank you for your order!"
    message = render_to_string(
        "orders/order_received_email.html",
        {
            "user": request.user,
            "order": order,
        },
    )
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # send order number and transaction id to sendData method via jsonResponse
    data = {
        "order_number": order.order_number,
        "transID": payment.payment_id,
    }
    return JsonResponse(data)


# Create your views here.
def place_order(request, total=0, quantity=0):
    current_user = request.user

    # if the cart count is less than or equal to 0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect("store")

    grand_total = 0
    tax = 0
    shipping = 0
    for cart_item in cart_items:
        total += int(cart_item.product.selling_price) * int(cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total) / 100
    shipping = 50
    grand_total = total + shipping + tax

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing info inside order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.phone = form.cleaned_data["phone"]
            data.email = form.cleaned_data["email"]
            data.address_line_1 = form.cleaned_data["address_line_1"]
            data.address_line_2 = form.cleaned_data["address_line_2"]
            data.city = form.cleaned_data["city"]
            data.country = form.cleaned_data["country"]
            data.state = form.cleaned_data["state"]
            data.order_note = form.cleaned_data["order_note"]
            data.order_total = grand_total
            data.tax = tax
            data.shipping = shipping
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()
            # generate order number
            yr = int(datetime.date.today().strftime("%Y"))
            dt = int(datetime.date.today().strftime("%d"))
            mt = int(datetime.date.today().strftime("%m"))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")  # 20230526
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(
                user=current_user, is_ordered=False, order_number=order_number
            )
            context = {
                "order": order,
                "cart_items": cart_items,
                "total": total,
                "tax": tax,
                "shipping": shipping,
                "grand_total": grand_total,
            }
            return render(request, "orders/payments.html", context)
        else:
            return redirect("store")

    else:
        return redirect("checkout")


def order_complete(request):
    order_number = request.GET.get("order_number")
    transID = request.GET.get("payment_id")

    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)

        subtotal = 0
        for i in ordered_products:
            subtotal += i.product_price * i.quantity
            shipping = 50

        payment = Payment.objects.get(payment_id=transID)

        context = {
            "order": order,
            "ordered_products": ordered_products,
            "order_number": order.order_number,
            "transID": payment.payment_id,
            "payment": payment,
            "subtotal": subtotal,
            "shipping": shipping,
        }

        return render(request, "orders/order_complete.html", context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect("home")

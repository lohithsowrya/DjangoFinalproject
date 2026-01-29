from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from productApp.models import Product


@login_required(login_url="login")
def place_order(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart_view")

    if request.method == "POST":
        for product_id, qty in cart.items():
            product = Product.objects.get(id=product_id)
            Order.objects.create(
                user=request.user,
                product=product,
                quantity=qty,
                total_price=product.price * qty
            )

        request.session["cart"] = {}  # clear cart
        return redirect("order_success")

    return render(request, "orderApp/order_confirm.html")

@login_required(login_url="login")
def order_success(request):
    return render(request, "orderApp/order_success.html")

@login_required(login_url="login")
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orderApp/my_orders.html", {"orders": orders})

@login_required(login_url="login")
def admin_orders(request):
    if not request.user.is_staff:
        return redirect("product_list")

    orders = Order.objects.all().order_by("-created_at")
    return render(request, "orderApp/admin_orders.html", {"orders": orders})

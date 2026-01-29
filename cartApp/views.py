from django.shortcuts import redirect, render
from productApp.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session["cart"] = cart
    return redirect("cart_view")

def cart_view(request):
    cart = request.session.get("cart", {})
    items = []
    total = 0

    for id, qty in cart.items():
        product = Product.objects.get(id=id)
        subtotal = product.price * qty
        total += subtotal
        items.append({
            "product": product,
            "qty": qty,
            "subtotal": subtotal
        })

    return render(request, "cartApp/cart.html", {"items": items, "total": total})
def update_cart(request, product_id):
    cart = request.session.get("cart", {})

    if request.method == "POST":
        qty = int(request.POST.get("quantity"))
        if qty > 0:
            cart[str(product_id)] = qty
        else:
            cart.pop(str(product_id))

    request.session["cart"] = cart
    return redirect("cart_view")
def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    cart.pop(str(product_id), None)
    request.session["cart"] = cart
    return redirect("cart_view")

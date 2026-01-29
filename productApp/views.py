from django.shortcuts import render,get_object_or_404
from .models import Product, Category

def product_list(request, category_id=None):
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, "productApp/product.html", {
        "products": products,
        "categories": categories
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "productApp/product_detail.html", {
        "product": product
    })
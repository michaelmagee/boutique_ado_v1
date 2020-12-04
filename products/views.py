""" Describe this """
from django.shortcuts import render
from .models import Product

def all_products(request):
    """ View for all products, inc sorting & searching """

    products = Product.objects.all()

    context = {
        "products": products,
    }


    return render(request, "products/products.html", context)

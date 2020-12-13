""" Describe this """
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

def all_products(request):
    """ View for all products, inc sorting & searching """

    products = Product.objects.all()
    categories = None
    direction = None
    query = None
    sort = None

    # Process the Get for Sort, categor or all request

    if request.GET:
        # handle a sort by request
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        # Handle a Category Request
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # handle a search request
        if 'q' in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criterea")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }


    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ View for individual product detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }


    return render(request, "products/product_detail.html", context)

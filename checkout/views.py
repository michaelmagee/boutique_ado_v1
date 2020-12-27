""" Describe me """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    """ Document me Mike """
    bag = request.session.get("bag", {})
    if not bag:
        # prevent people from manually accessing the URL by typing /checkout
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51I34iULW6jaQl80yYc7ur2ealzSCSzk541oiFk39YvLAJe3eX81hfDHd4Kwc2dL9PygRDoOfxCTJHM1xCevhgBRT00NIgOHDBn",
        "client_secret": "test client secret",
    }

    return render(request, template, context)

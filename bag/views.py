""" Describe this """
from django.shortcuts import render


def view_bag(request):
    """ Renders the bag contents """
    return render(request, "bag/bag.html")

""" Describe me """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Describe me """
    name = 'checkout'

    def ready(self):
        """ Describe me """
        import checkout.signals

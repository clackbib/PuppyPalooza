from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^remove/(\d+)/$', 'cart.views.remove_from_cart', name="cart_remove"),
    url(r'^checkout/$', 'cart.views.checkout', name="cart_checkout"),

    url(r'^success/', TemplateView.as_view(template_name='cart/success.html'), name="cart_win"),
    url(r'^cancel/', TemplateView.as_view(template_name='cart/cancel.html'), name="cart_cancel"),
    url(r'^ipn/$', 'cart.views.payment_successful', name="cart_ipn"),
)

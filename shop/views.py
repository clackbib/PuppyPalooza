# Create your views here.
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from shop.models import Puppy

def shop_home(request):
    puppies = Puppy.objects.all()
    paypal_dict = {
        "business": "yourpaypalemail@example.com",
        "amount": "0",
        "item_name": "Item name",
        "invoice": "unique-invoice-id",
        "notify_url": "http://www.example.com/your-ipn-location/",
        "return_url": "http://www.example.com/your-return-location/",
        "cancel_return": "http://www.example.com/your-cancel-location/",
        }
    for p in puppies:
        paypal_dict["amount"] = str(p.price)
        paypal_dict["item_name"] = str(p.puppy_name)
        p.buy_form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, "shop/shop_home.html", locals())



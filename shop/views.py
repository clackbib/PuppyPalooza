# Create your views here.
import random
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from shop.models import Puppy
from cart.models import CartItem

def shop_home(request):
    id = random.randint(1, 1)
    day_puppy = Puppy.objects.get(id = id)

    CartItem.objects.add_to_cart(day_puppy,request.user, day_puppy.price,None)
    puppies = Puppy.objects.all()

    for p in puppies:
        p.buy_form = PayPalPaymentsForm(initial={
        "business": "yourpaypalemail@example.com",
        "amount": str(p.price),
        "item_name": str(p.puppy_name),
        "invoice": "unique-invoice-id",
        "notify_url": "http://www.example.com/your-ipn-location/",
        "return_url": "http://www.example.com/your-return-location/",
        "cancel_return": "http://www.example.com/your-cancel-location/",
        })

    return render(request, "shop/shop_home.html", locals())

def checkout(request):
    items = CartItem.objects.filter(user = request.user)
    item_names = ""
    total = 0
    for i in items:
        item_names += str(i.object.puppy_name)+" ,"
        total+= i.amount

    return render(request, "shop/checkout.html", locals())




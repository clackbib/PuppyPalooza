# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from paypal.standard.forms import PayPalPaymentsForm
from shop.models import Puppy
from cart.models import CartItem

def shop_home(request):
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

@login_required(login_url="home.views.home")
def add_puppy(request,puppy_id):
    puppy = Puppy.objects.get(id = puppy_id)
    CartItem.objects.add_to_cart(puppy,request.user, puppy.price,None)
    count = 0
    items = CartItem.objects.filter(user = request.user)
    for i in items:
        count += 1

    request.session['cart_count'] = count
    return redirect("shop.views.shop_home")

@login_required(login_url="home.views.home")
def checkout(request):
    items = CartItem.objects.filter(user = request.user)
    checkout_dict = {
        "business": "yourpaypalemail@example.com",
        "invoice": "unique-invoice-id",
        "item_name":"Stuff",
        "notify_url": "http://www.example.com/your-ipn-location/",
        "return_url": "http://www.example.com/your-return-location/",
        "cancel_return": "http://www.example.com/your-cancel-location/",
        }
    total = 0
    count = 0
    puppies_str = ""
    for i in items:
        puppies_str += str(i.object.puppy_name) + ","
        total+= i.amount
        count += 1

    request.session['cart_count'] = count
    checkout_dict['item_name'] = str(puppies_str)
    checkout_dict['amount'] = str(total)
    form = PayPalPaymentsForm(initial= checkout_dict)
    if request.session['cart_count'] <=  0:
        return redirect("home.views.home_page")

    return render(request, "shop/checkout.html", locals())




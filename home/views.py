# Create your views here.]
import random
from django.shortcuts import render
from login.forms import ConnectionForm
from shop.models import Puppy
from cart.models import CartItem


def home_page(request):

    max_count = Puppy.objects.all().count()
    id = random.randint(1, max_count)
    day_puppy = Puppy.objects.get(id = id)

    count = 0
    if request.user.is_authenticated():
        items = CartItem.objects.filter(user = request.user)
        for i in items:
            count += 1
        request.session['cart_count'] = count

    return render(request, "home/home.html", locals())
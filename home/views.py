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
    #CartItem.objects.add_to_cart(day_puppy,request.user, day_puppy.price,None)

    if request.method == 'POST':
        stuff = "done"
    else:
        form = ConnectionForm()
    return render(request, "home/home.html", locals())
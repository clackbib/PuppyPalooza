# Create your views here.]
import random
from django.shortcuts import render
from login.forms import ConnectionForm
from shop.models import Puppy


def home_page(request):
    max_count = Puppy.objects.all().count()
    id = random.randint(1, max_count)
    day_puppy = Puppy.objects.get(id = id)
    if request.method == 'POST':
        stuff = "done"
    else:
        form = ConnectionForm()
    return render(request, "home/home.html", locals())
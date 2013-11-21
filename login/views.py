# Create your views here.
from login.forms import ConnectionForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import  redirect
from django.core.urlresolvers import reverse

def connect(request):
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                request.session["logged"] = True

    else:
        form = ConnectionForm()
    return redirect("home.views.home_page")

def disconnect(request):
    logout(request)
    return redirect(reverse("home.views.home_page"))
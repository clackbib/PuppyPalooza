# Create your views here.
from login.forms import ConnectionForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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

def register(request):
    error = False
    message = ""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            complete = True
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email)
            user2 = User.objects.filter(username=username)

            if user:
                message = "Email address already in use"
                error = True
            elif user2:
                message = "Username already in use"
                error = True
            else:
                user3 = User.objects.create_user(username, email, password)
                return redirect("home.views.home_page")

        else:
            error = True
            message = "Fields incomplete."
    else:
        form = RegistrationForm()
    return render(request, "home/register.html", locals())
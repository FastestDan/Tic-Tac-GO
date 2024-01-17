from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
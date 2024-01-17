from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Как же меня всё это заебало! ЗА-Е-БА-ЛО!")


def home(response):
    return render(response, "main/home.html", {})

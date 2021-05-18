from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def hello(request):
    userName = request.GET['name']
    return render(request, "hello.html", {'userName': userName})

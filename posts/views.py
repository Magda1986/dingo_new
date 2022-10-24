from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def post(request):
    t = loader.get_template("posts/main.html")
    return HttpResponse(t.render())

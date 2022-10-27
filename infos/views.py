from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def infos(request):
    nazwa = "Magda Ratajczak"
    t = loader.get_template("infos/main.html")
    c={"nazwa": nazwa}
    return HttpResponse(t.render(c))

def me(request):
    nazwa = "O mnie"
    t = loader.get_template("infos/me.html")
    c={"nazwa" : nazwa}
    return HttpResponse(t.render(c))

def contact(request):
    nazwa = "Kontakt"
    t = loader.get_template("infos/contact.html")
    c={"nazwa": nazwa}
    return HttpResponse(t.render(c))

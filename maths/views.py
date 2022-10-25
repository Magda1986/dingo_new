from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def math(request):
    t = loader.get_template("maths/main.html")
    return HttpResponse(t.render())


def add(request, a, b):
    a, b = int(a), int(b)
    result = a + b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "+", "wynik": result, "title": "dodawanie"}
    return HttpResponse(t.render(c))


def sub(request, a, b):
    a, b = int(a), int(b)
    result = a - b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "-", "wynik": result, "title": "odejmowanie"}
    return HttpResponse(t.render(c))


def mul(request, a, b):
    a, b = int(a), int(b)
    result = a * b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "*", "wynik": result, "title": "mnożenie"}
    return HttpResponse(t.render(c))


def div(request, a, b):
    a, b = int(a), int(b)
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    result = a / b
    t = loader.get_template("maths/operation.html")
    c = {"a": a, "b": b, "operacja": "/", "wynik": result, "title": "dzielenie"}
    return HttpResponse(t.render(c))

def maths_list(request):
    maths = Math.objects.all()
    return render(
        request=request,
        template_name="maths/list.html",
        context={"maths": maths}
    )

def math_details(request, id):
    math = Math.objects.get(id=id)
    return render(
        request=request,
        template_name="maths/details.html",
        context={"math": math}
    )



#def div(request, a, b):
 #  a, b = int(a), int(b)
  # if b == 0:
   #    return HttpResponse("Nie dziel przez 0")
   #return HttpResponse(a / b)

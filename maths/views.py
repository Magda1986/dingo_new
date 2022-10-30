from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import ResultForm
from .models import Result, Math


def math(request):
    t = loader.get_template("maths/main.html")
    return HttpResponse(t.render())


#def add(request, a, b):
    #a, b = int(a), int(b)
    #wynik = a + b
    #t = loader.get_template("maths/operation.html")
    #c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}
    #return HttpResponse(t.render(c))

def add(request, a, b):
    wynik = a + b
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='add', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


#def sub(request, a, b):
    #a, b = int(a), int(b)
    #wynik = a - b
    #t = loader.get_template("maths/operation.html")
    #c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "odejmowanie"}
    #return HttpResponse(t.render(c))

def sub(request, a, b):
    wynik = a - b
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "odejmowanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='sub', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


#def mul(request, a, b):
    #a, b = int(a), int(b)
    #wynik = a * b
    #t = loader.get_template("maths/operation.html")
    #c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "mnożenie"}
    #return HttpResponse(t.render(c))

def mul(request, a, b):
    wynik = a * b
    c = {"a": a, "b": b, "operacja": "*", "wynik": wynik, "title": "mnożenie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='mul', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


#def div(request, a, b):
    #a, b = int(a), int(b)
    #if b == 0:
        #return HttpResponse("Nie dziel przez 0")
    #wynik = a / b
    #t = loader.get_template("maths/operation.html")
    #c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
    #return HttpResponse(t.render(c))

def div(request, a, b):
    if b==0:
        return HttpResponse("Nie dziel przez 0")
    wynik = a / b
    c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='div', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )


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

#def results_list(request):
#    if request.method == "POST":
#        value = request.POST['value'] or None
#        error = request.POST['error'] or None
#        if value and error:
#            messages.add_message(
#                request,
#                messages.ERROR,
#                "Błąd! Podano jednocześnie value i error. Podaj tylko jedną z tych wartości"
#            )
#        elif value or error:

#            Result.objects.get_or_create(
#                value=float(value),
#                error=error
#            )
#            messages.add_message(
#                request,
#                messages.SUCCESS,
#                "Utworzono nowy Result!!"
#            )

#        else:
#            messages.add_message(
#                request,
#                messages.ERROR,
#                "Błąd! Nie podano wartości!!"
#            )

#    results = Result.objects.all()
 #   return render(
  #      request=request,
   #     template_name="maths/results.html",
    #    context={"results": results}
    #)


def results_list(request):
    if request.method == "POST":
        form = ResultForm(data=request.POST)

        if form.is_valid():

            print(form.cleaned_data)
            print(Result.objects.get(**form.cleaned_data))

            Result.objects.get_or_create(form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy Result!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = ResultForm()
    results = Result.objects.all()
    return render(
        request=request,
        template_name="maths/results.html",
        context={
            "results": results,
            "form": form
        }
    )

#def div(request, a, b):
 #  a, b = int(a), int(b)
  # if b == 0:
   #    return HttpResponse("Nie dziel przez 0")
   #return HttpResponse(a / b)

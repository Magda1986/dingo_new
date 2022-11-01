from django.http import HttpResponse
from django.template import loader


# def greetings(request):
#     return HttpResponse("Hello Lord in my World!! :) ")

def greetings(request):
    nazwa = "Strona Główna"
    t = loader.get_template("greetings/greetings.html")
    c={"nazwa": nazwa}
    return HttpResponse(t.render(c))

def personal_greeting(request, a):
    return HttpResponse(f"Hello {a.capitalize()} in my World!!! :) ")
from django.urls import path
from .views import greetings, personal_greeting


urlpatterns = [

    path('', greetings),
    path('<a>', personal_greeting),

]


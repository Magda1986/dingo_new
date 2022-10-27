from django.urls import path
from .views import me, contact, infos

urlpatterns = [
   path('', infos),
   path('me/', me),
   path('contact/', contact)
]
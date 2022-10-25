# maths/admin.py
from django.contrib import admin
from maths.models import Math, Result
# Register your models here.

class MathAdmin(admin.ModelAdmin):
    list_display = ["id", "operation", "a", "b", "created", "result"]    #to lista kolumn widoczna na liście
    list_filter = ["operation"]    #dodaje boczny panel z filtrami,
    search_fields = ["a", "b"]  #dodaje pole wyszukiwania. Wyszukiwanie odbywa się we wskazanych kolumnach

admin.site.register(Math, MathAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'error']
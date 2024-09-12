from django.contrib import admin

# Register your models here.

from .models import Küsimus, Valikvastus

admin.site.register(Küsimus)
admin.site.register(Valikvastus)
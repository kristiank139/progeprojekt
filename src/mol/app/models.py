from django.db import models

# Create your models here.

class Küsimus(models.Model):
    küsimus_tekst = models.CharField(max_length=200)

class Valikvastus(models.Model):
    vastus_tekst = models.CharField(max_length=200)
    küsimus = models.ForeignKey(Küsimus, on_delete=models.CASCADE)

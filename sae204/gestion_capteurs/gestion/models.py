from django.db import models

# Create your models here.

class Capteur(models.Model):
    idcapteur = models.IntegerField(unique=True)
    nom = models.CharField(max_length=100, unique=True)
    piece = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Donnees(models.Model):
    capteur = models.ForeignKey (Capteur, on_delete=models.CASCADE)
    jour = models.DateField()
    heure = models.TimeField()
    temp = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"capteur {self.idcapteur} le {self.jour} a {self.heure} température {self.temp}"



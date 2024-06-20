from django import forms
from .models import Capteur, Donnees

class CapteurForm(forms.ModelForm):
    class Meta:
        model = Capteur
        fields = ['idcapteur', 'nom', 'piece', 'emplacement']
        labels = {
            'idcapteur': 'Numéro Capteur',
            'nom': 'Nom',
            'piece': 'Pièce',
            'emplacement': 'Emplacement',
        }

class DonneesForm(forms.ModelForm):
    class Meta:
        model = Donnees
        fields = ['capteur', 'jour', 'heure', 'temp']
        labels = {
            'capteur': 'Capteur',
            'jour': 'Jour',
            'heure': 'Heure',
            'temp': 'Température (deg C)',
        }
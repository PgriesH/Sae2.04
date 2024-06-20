from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Capteur, Donnees
from .forms import CapteurForm, DonneesForm
from datetime import datetime
from django.contrib import messages
import csv
from django.db.models import Q
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Vue pour la page d'accueil
def home(request):
    return render(request, 'gestion/home.html')

def list_capteurs(request):
    capteurs = Capteur.objects.all()
    return render(request, 'gestion/capteurs/list_capteurs.html', {'capteurs': capteurs})

def create_capteur(request):
    if request.method == 'POST':
        form = CapteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_capteurs')
    else:
        form = CapteurForm()
    return render(request, 'gestion/capteurs/form_capteur.html', {'form': form})

def update_capteur(request, pk):
    capteur = get_object_or_404(Capteur, pk=pk)
    if request.method == 'POST':
        form = CapteurForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return redirect('list_capteurs')
    else:
        form = CapteurForm(instance=capteur)
    return render(request, 'gestion/capteurs/form_capteur.html', {'form': form})

def delete_capteur(request, pk):
    capteur = get_object_or_404(Capteur, pk=pk)
    capteur.delete()
    return redirect('list_capteurs')

def detail_capteur(request, pk):
    capteur = get_object_or_404(Capteur, pk=pk)
    return render(request, 'gestion/capteurs/detail_capteur.html', {'capteur': capteur})

def list_donnees(request):
    donnees = Donnees.objects.all()
    return render(request, 'gestion/donnees/list_donnees.html', {'donnees': donnees})

def create_donnee(request):
    if request.method == 'POST':
        form = DonneesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_donnees')
    else:
        form = DonneesForm()
    return render(request, 'gestion/donnees/form_donnee.html', {'form': form})

def update_donnee(request, pk):
    donnee = get_object_or_404(Donnees, pk=pk)
    if request.method == 'POST':
        form = DonneesForm(request.POST, instance=donnee)
        if form.is_valid():
            form.save()
            return redirect('list_donnees')
    else:
        form = DonneesForm(instance=donnee)
    return render(request, 'gestion/donnees/form_donnee.html', {'form': form})

def delete_donnee(request, pk):
    donnee = get_object_or_404(Donnees, pk=pk)
    donnee.delete()
    return redirect('list_donnees')

def detail_donnee(request, pk):
    donnee = get_object_or_404(Donnees, pk=pk)
    return render(request, 'gestion/donnees/detail_donnee.html', {'donnee': donnee})


def donnee_fiche(request):
    capteur_id = request.GET.get('capteur_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    donnees = Donnees.objects.all()
    if capteur_id:
        donnees = donnees.filter(capteur_id=capteur_id)
    if start_date and end_date:
        donnees = donnees.filter(jour__range=[start_date, end_date])

    capteurs = Capteur.objects.all()
    return render(request, 'gestion/donnees/donnee_fiche.html', {'donnees': donnees, 'capteurs': capteurs})


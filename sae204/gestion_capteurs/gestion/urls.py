from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('capteurs/', views.list_capteurs, name='list_capteurs'),
    path('capteurs/add/', views.create_capteur, name='add_capteur'),
    path('capteurs/edit/<int:pk>/', views.update_capteur, name='edit_capteur'),
    path('capteurs/delete/<int:pk>/', views.delete_capteur, name='delete_capteur'),
    path('capteurs/view/<int:pk>/', views.detail_capteur, name='view_capteur'),

    path('donnees/', views.list_donnees, name='list_donnees'),
    path('donnees/add/', views.create_donnee, name='add_donnee'),
    path('donnees/edit/<int:pk>/', views.update_donnee, name='edit_donnee'),
    path('donnees/delete/<int:pk>/', views.delete_donnee, name='delete_donnee'),
    path('donnees/view/<int:pk>/', views.detail_donnee, name='view_donnee'),

    path('donnee_fiche/', views.donnee_fiche, name='donnee_fiche'),

]
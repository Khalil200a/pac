from .models import *
from django.views import generic
from django.shortcuts import render
from django.template import RequestContext

def detail(request):
    produits = Produit.objects.all()
    formations = Formation.objects.all()
    consultings = Consulting.objects.all()
    prestations = Prestation.objects.all()
    filters = Filters.objects.all()
    context = {'produits': produits, 'formations': formations, 'consultings': consultings, 'prestations': prestations, 'filters':filters}
    return render(request, 'index.html', context=context)

def pro(request):
    produits = Produit.objects.all()
    formations = Formation.objects.all()
    consultings = Consulting.objects.all()
    prestations = Prestation.objects.all()
    filters = Filters.objects.all()
    context = {'produits': produits, 'formations': formations, 'consultings': consultings, 'prestations': prestations, 'filters':filters}
    return render(request, 'produit.html', context=context)
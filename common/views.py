from .models import *
from django.views import generic


class HomeView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'produits'

    def get_queryset(self):
        return Produit.objects.all()


class ProduitView(generic.ListView):
    template_name = 'produit.html'
    context_object_name = 'produits'

    def get_queryset(self):
        return Produit.objects.all()

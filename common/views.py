from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from userprofile.models import Profile
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

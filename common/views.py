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


class HomeView(TemplateView):
    template_name = 'index.html'

class ProduitView(LoginRequiredMixin, generic.ListView):
    template_name = 'common/produit.html'
    login_url = reverse_lazy('home')
    context_object_name = 'format'

    def get_queryset(self):
        return Produit.objects.all()

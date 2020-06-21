# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from devis.models import Devis, Client, Prestation
from .forms import PrestationAjoutForm, DevisAjoutForm, DevisModifForm


def oral_ecrit(request):
    return render(request, 'devis/devis_creation_oral_ecrit.html')

def devis_pneu_oral(request):
    return render(request, 'devis/devis_pneu_oral.html')

def devis_creation_ecrit(request):
    return render(request, 'devis/devis_creation_ecrit.html')

class DevisUpdate(UpdateView):
    model = Devis
    template_name = "devis/devis_update.html"
    form_class = DevisModifForm
    success_url = reverse_lazy("liste_devis")

    def form_valid(self, form):
        self.object = form.save()

        messages.success(self.request, "Devis modifié avec succès !")
        return HttpResponseRedirect(self.get_success_url())

class DevisCreate(CreateView):
    model = Devis
    template_name = "devis/devis_creer.html"
    form_class = DevisAjoutForm
    success_url = reverse_lazy("liste_devis")

    def form_valid(self, form):
        self.object = form.save()

        messages.success(self.request, "Devis créé avec succès !")
        return HttpResponseRedirect(self.get_success_url())


class PrestationCreate(CreateView):
    model = Prestation
    template_name = "devis/prestation_creer.html"
    form_class = PrestationAjoutForm
    success_url = reverse_lazy("liste_prestations")


class ListeClients(ListView):
    model = Client
    context_object_name = "clients"
    template_name = "client_list"
    paginate_by = 10


class ListePrestation(ListView):
    model = Prestation
    context_object_name = "prestations"
    template_name = "prestation_list"
    paginate_by = 10


class ListeDevis(ListView):
    model = Devis
    context_object_name = "devis"
    template_name = "devis_list"
    paginate_by = 10


class DevisDetail(DetailView):
    context_object_name = "devis"
    model = Devis
    template_name = "devis/devis_detail.html"

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from hikes.forms import ExpeditionForm
from hikes.models import (
    Hiker,
    Expedition,
    Region,
)


@login_required
def index(request):
    num_hikers = Hiker.objects.count()
    num_expeditions = Expedition.objects.count()
    num_regions = Region.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_hikers": num_hikers,
        "num_expeditions": num_expeditions,
        "num_regions": num_regions,
        "num_visits": num_visits + 1,
    }

    return render(request, "hikes/index.html", context=context)


class RegionListView(LoginRequiredMixin, ListView):
    model = Region


class RegionCreateView(LoginRequiredMixin, CreateView):
    model = Region
    fields = "__all__"
    success_url = reverse_lazy("hikes:region-list")


class RegionUpdateView(LoginRequiredMixin, UpdateView):
    model = Region
    fields = "__all__"
    success_url = reverse_lazy("hikes:region-list")


class RegionDeleteView(LoginRequiredMixin, DeleteView):
    model = Region
    success_url = reverse_lazy("hikes:region-list")


class HikerListView(LoginRequiredMixin, ListView):
    model = Hiker


class HikerDetailView(LoginRequiredMixin, DetailView):
    model = Hiker


class ExpeditionListView(LoginRequiredMixin, ListView):
    model = Expedition


class ExpeditionDetailView(LoginRequiredMixin, DetailView):
    model = Expedition


class ExpeditionCreateView(LoginRequiredMixin, CreateView):
    model = Expedition
    form_class = ExpeditionForm
    success_url = reverse_lazy("hikes:expedition-list")


class ExpeditionUpdateView(LoginRequiredMixin, UpdateView):
    model = Expedition
    form_class = ExpeditionForm
    success_url = reverse_lazy("hikes:expedition-list")


class ExpeditionDeleteView(LoginRequiredMixin, DeleteView):
    model = Expedition
    success_url = reverse_lazy("hikes:expedition-list")

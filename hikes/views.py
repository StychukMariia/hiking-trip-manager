from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class HikerListView(LoginRequiredMixin, ListView):
    model = Hiker


class HikerDetailView(LoginRequiredMixin, DetailView):
    model = Hiker


class ExpeditionListView(LoginRequiredMixin, ListView):
    model = Expedition


class ExpeditionDetailView(LoginRequiredMixin, DetailView):
    model = Expedition

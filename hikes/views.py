from django.shortcuts import render
from django.views.generic import ListView, DetailView

from hikes.models import (
    Hiker,
    Expedition,
    Region
)


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


class HikerListView(ListView):
    model = Hiker


class HikerDetailView(DetailView):
    model = Hiker

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from hikes.forms import (
    ExpeditionForm,
    HikerCreationForm,
    HikerUpdateForm, HikerUsernameSearchForm, RegionNameSearchForm, ExpeditionTitleSearchForm
)
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

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super(RegionListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = RegionNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Region.objects.all()
        form = RegionNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HikerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")

        context["search_form"] = HikerUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Hiker.objects.all()
        form = HikerUsernameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class HikerDetailView(LoginRequiredMixin, DetailView):
    model = Hiker


class HikerCreateView(LoginRequiredMixin, CreateView):
    model = Hiker
    form_class = HikerCreationForm


class HikerUpdateView(LoginRequiredMixin, UpdateView):
    model = Hiker
    form_class = HikerUpdateForm


class HikerDeleteView(LoginRequiredMixin, DeleteView):
    model = Hiker
    success_url = reverse_lazy("hikes:hiker-list")


class ExpeditionListView(LoginRequiredMixin, ListView):
    model = Expedition

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ExpeditionListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")

        context["search_form"] = ExpeditionTitleSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Expedition.objects.all()
        form = ExpeditionTitleSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return queryset


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

from django.urls import path
from .views import (
    index,
    HikerListView,
    HikerDetailView,
    RegionListView,
    ExpeditionListView,
    ExpeditionDetailView,
    RegionCreateView,
    RegionUpdateView,
    RegionDeleteView,
    ExpeditionDeleteView,
    ExpeditionCreateView,
    ExpeditionUpdateView,
    HikerDeleteView,
    HikerCreateView, HikerUpdateView, toggle_participation_to_expedition,
)

app_name = "hikes"

urlpatterns = [
    path("", index, name="index"),
    path("regions/", RegionListView.as_view(), name="region-list"),
    path(
        "regions/create/",
        RegionCreateView.as_view(),
        name="region-create"
    ),
    path(
        "regions/<int:pk>/update/",
        RegionUpdateView.as_view(),
        name="region-update"
    ),
    path(
        "regions/<int:pk>/delete/",
        RegionDeleteView.as_view(),
        name="region-delete"
    ),
    path("hikers/", HikerListView.as_view(), name="hiker-list"),
    path(
        "hikers/<int:pk>/",
        HikerDetailView.as_view(),
        name="hiker-detail"
    ),
    path(
        "hikers/create/",
        HikerCreateView.as_view(),
        name="hiker-create"
    ),
    path(
        "hikers/<int:pk>/update/",
        HikerUpdateView.as_view(),
        name="hiker-update"
    ),
    path(
        "hikers/<int:pk>/delete/",
        HikerDeleteView.as_view(),
        name="hiker-delete"
    ),
    path(
        "expeditions/",
        ExpeditionListView.as_view(),
        name="expedition-list"
    ),
    path(
        "expeditions/<int:pk>/",
        ExpeditionDetailView.as_view(),
        name="expedition-detail"
    ),
    path(
        "expeditions/create/",
        ExpeditionCreateView.as_view(),
        name="expedition-create"
    ),
    path(
        "expeditions/<int:pk>/update/",
        ExpeditionUpdateView.as_view(),
        name="expedition-update"
    ),
    path(
        "expeditions/<int:pk>/delete/",
        ExpeditionDeleteView.as_view(),
        name="expedition-delete"
    ),
    path(
        "expeditions/<int:pk>/toggle_participation/",
        toggle_participation_to_expedition,
        name="expedition-toggle-participation"
    ),
]

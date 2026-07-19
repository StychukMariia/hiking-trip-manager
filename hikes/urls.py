from django.urls import path
from .views import (
    index,
    HikerListView,
    HikerDetailView,
    RegionListView,
    ExpeditionListView,
    ExpeditionDetailView,
)

app_name = "hikes"

urlpatterns = [
    path("", index, name="index"),
    path("regions/", RegionListView.as_view(), name="region-list"),
    path("hikers/", HikerListView.as_view(), name="hiker-list"),
    path(
        "hikers/<int:pk>/",
        HikerDetailView.as_view(),
        name="hiker-detail"
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
]

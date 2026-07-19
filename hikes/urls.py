from django.urls import path
from .views import (
    index,
    HikerListView,
    HikerDetailView,
    RegionListView
)

app_name = "hikes"

urlpatterns = [
    path("", index, name="index"),
    path("regions/", RegionListView.as_view(), name="region-list"),
    path("hikers/", HikerListView.as_view(), name="hiker-list"),
    path("hikers/<int:pk>/", HikerDetailView.as_view(), name="hiker-detail"),
]
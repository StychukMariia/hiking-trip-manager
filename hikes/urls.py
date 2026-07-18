from django.urls import path
from .views import (
    index,
    HikerListView,
    HikerDetailView
)

app_name = "hikes"

urlpatterns = [
    path("", index, name="index"),
    path("hikers/", HikerListView.as_view(), name="hiker-list"),
    path("hikers/<int:pk>/", HikerDetailView.as_view(), name="hiker-detail"),
]
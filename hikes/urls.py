from django.urls import path
from .views import index

app_name = "hikes"

urlpatterns = [
    path("", index, name="index"),
]
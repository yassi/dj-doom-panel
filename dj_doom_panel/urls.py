from django.urls import path
from . import views

app_name = "dj_doom_panel"

urlpatterns = [
    path("", views.index, name="index"),
]

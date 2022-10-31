from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "vtwi"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

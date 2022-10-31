from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import home_view, index_view

app_name = "vtwi"

urlpatterns = [
    path("", index_view, name="index"),
    path("home/", home_view, name="home"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("__admin__/", admin.site.urls),
    path("", include("social_django.urls")),
    path("", include("vtwi.urls")),
]

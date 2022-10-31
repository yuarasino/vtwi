from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "vtwi/index.html"


class HomeView(TemplateView, LoginRequiredMixin):
    template_name = "vtwi/home.html"

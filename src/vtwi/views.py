from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import VTwiUserForm


def index_view(request):
    return render(request, "vtwi/index.html")


@login_required
def home_view(request):
    vtwi_user_form = VTwiUserForm(request.POST or None, instance=request.user)
    if request.method == "POST":
        form_type = request.POST.get("form_type") or ""
        if form_type == "vtwi_user":
            if vtwi_user_form.is_valid():
                vtwi_user_form.save()
                return redirect("vtwi:home")
    context = {
        "vtwi_user_form": vtwi_user_form,
    }
    return render(request, "vtwi/home.html", context)
